# Range-Scalp Bot

*Updated Mon Nov 16 03:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61665 | 53814 | 7851 (115) | 3 | $-16554.77 | -4.3% |
| **+10¢** | 46063 | 36863 | 9200 (157) | 3 | $-15500.08 | -5.4% |
| **+15¢** | 38595 | 28672 | 9923 (196) | 5 | $-14122.36 | -5.8% |
| **+20¢** | 34404 | 23995 | 10409 (249) | 5 | $-12351.65 | -5.7% |
| **+10¢ (15¢ stop)** | 75046 | 74892 | 154 (90) | 0 | $-27631.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 03:57 | +10 stop | HYPE | DOWN | 0.53 | 0.33 | -2.34 |
| 11-16 03:57 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-16 03:57 | +15 | HYPE | DOWN | 0.54 | 0.70 | 1.27 |
| 11-16 03:57 | +10 | HYPE | DOWN | 0.54 | 0.70 | 1.27 |
| 11-16 03:57 | +5 | HYPE | DOWN | 0.56 | 0.62 | 0.25 |
| 11-16 03:56 | +10 stop | XRP | UP | 0.67 | 0.49 | -2.14 |
| 11-16 03:56 | +10 | XRP | UP | 0.67 | 0.82 | 1.22 |
| 11-16 03:56 | +5 | XRP | UP | 0.67 | 0.77 | 0.70 |
| 11-16 03:56 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 11-16 03:56 | +20 | XRP | DOWN | 0.48 | open |  |
| 11-16 03:56 | +15 | XRP | DOWN | 0.48 | open |  |
| 11-16 03:56 | +10 | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 11-16 03:56 | +5 | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 11-16 03:55 | +5 | BTC | DOWN | 0.54 | open |  |
| 11-16 03:55 | +10 stop | ETH | UP | 0.60 | 0.75 | 1.19 |
| 11-16 03:55 | +20 | ETH | UP | 0.60 | 0.82 | 1.92 |
| 11-16 03:55 | +10 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 11-16 03:55 | +5 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 11-16 03:55 | +10 stop | ZEC | DOWN | 0.62 | 0.42 | -2.35 |
| 11-16 03:55 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-16 03:55 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-16 03:55 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-16 03:55 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
| 11-16 03:55 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-16 03:55 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-16 03:55 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-16 03:55 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 03:53 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-16 03:52 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-16 03:52 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-16 03:52 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-16 03:52 | +10 stop | BNB | UP | 0.70 | 0.52 | -2.13 |
| 11-16 03:52 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-16 03:52 | +10 stop | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 03:52 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-16 03:52 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 03:52 | +10 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 03:52 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-16 03:52 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 03:52 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
