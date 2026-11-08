# Range-Scalp Bot

*Updated Sun Nov 08 00:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51739 | 45117 | 6622 (80) | 2 | $-14324.27 | -4.4% |
| **+10¢** | 38612 | 30891 | 7721 (106) | 2 | $-13319.61 | -5.5% |
| **+15¢** | 32335 | 24014 | 8321 (135) | 2 | $-12206.38 | -6.0% |
| **+20¢** | 28763 | 20039 | 8724 (180) | 3 | $-10751.88 | -6.0% |
| **+10¢ (15¢ stop)** | 62995 | 62892 | 103 (61) | 1 | $-23313.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 00:38 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 11-08 00:38 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-08 00:38 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-08 00:38 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-08 00:38 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-08 00:38 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 11-08 00:38 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-08 00:38 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-08 00:38 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-08 00:38 | +5 | NEAR | DOWN | 0.66 | open |  |
| 11-08 00:37 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-08 00:37 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-08 00:37 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 00:37 | +5 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 00:32 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.47 |
| 11-08 00:32 | +20 | BNB | DOWN | 0.65 | 0.91 | 2.36 |
| 11-08 00:32 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.47 |
| 11-08 00:32 | +10 | BNB | DOWN | 0.64 | 0.82 | 1.52 |
| 11-08 00:32 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-08 00:30 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.78 |
| 11-08 00:30 | +20 | HYPE | DOWN | 0.69 | 0.91 | 1.90 |
| 11-08 00:30 | +15 | HYPE | DOWN | 0.69 | 0.89 | 1.73 |
| 11-08 00:30 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.78 |
| 11-08 00:30 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.37 |
| 11-08 00:30 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 00:30 | +20 | ZEC | DOWN | 0.64 | open |  |
| 11-08 00:30 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-08 00:30 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 00:30 | +5 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 00:30 | +10 stop | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 00:30 | +20 | XRP | DOWN | 0.63 | 0.87 | 2.15 |
| 11-08 00:30 | +15 | XRP | DOWN | 0.63 | 0.87 | 2.15 |
| 11-08 00:30 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 00:30 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 11-08 00:30 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-08 00:30 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-08 00:30 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-08 00:30 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-08 00:30 | +5 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-08 00:30 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
