# Range-Scalp Bot

*Updated Sun Nov 15 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60151 | 52470 | 7681 (107) | 1 | $-16369.61 | -4.3% |
| **+10¢** | 44945 | 35944 | 9001 (143) | 1 | $-15450.93 | -5.5% |
| **+15¢** | 37660 | 27954 | 9706 (181) | 1 | $-14088.28 | -6.0% |
| **+20¢** | 33559 | 23376 | 10183 (233) | 1 | $-12415.48 | -5.9% |
| **+10¢ (15¢ stop)** | 73241 | 73098 | 143 (82) | 0 | $-26968.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 01:38 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.85 |
| 11-15 01:38 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 11-15 01:38 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.28 |
| 11-15 01:38 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.75 |
| 11-15 01:38 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-15 01:38 | +20 | ZEC | DOWN | 0.68 | 0.90 | 1.97 |
| 11-15 01:38 | +15 | ZEC | DOWN | 0.68 | 0.90 | 1.97 |
| 11-15 01:38 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-15 01:38 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-15 01:34 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-15 01:33 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-15 01:33 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-15 01:33 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-15 01:33 | +10 stop | XRP | DOWN | 0.69 | 0.84 | 1.26 |
| 11-15 01:32 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 11-15 01:32 | +10 stop | ETH | UP | 0.63 | 0.41 | -2.54 |
| 11-15 01:32 | +10 stop | BTC | UP | 0.62 | 0.43 | -2.25 |
| 11-15 01:32 | +20 | BTC | UP | 0.62 | open |  |
| 11-15 01:32 | +15 | BTC | UP | 0.61 | open |  |
| 11-15 01:32 | +10 | BTC | UP | 0.61 | open |  |
| 11-15 01:32 | +5 | BTC | UP | 0.61 | open |  |
| 11-15 01:32 | +5 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 11-15 01:32 | +10 stop | NEAR | DOWN | 0.56 | 0.79 | 2.03 |
| 11-15 01:32 | +20 | NEAR | DOWN | 0.54 | 0.79 | 2.20 |
| 11-15 01:32 | +15 | NEAR | DOWN | 0.54 | 0.79 | 2.20 |
| 11-15 01:32 | +10 | NEAR | DOWN | 0.54 | 0.79 | 2.20 |
| 11-15 01:32 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 11-15 01:32 | +5 | ETH | DOWN | 0.51 | 0.58 | 0.34 |
| 11-15 01:31 | +10 stop | ZEC | DOWN | 0.58 | 0.41 | -2.05 |
| 11-15 01:31 | +20 | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 11-15 01:31 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.39 |
| 11-15 01:31 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.98 |
| 11-15 01:31 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.98 |
| 11-15 01:31 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.30 |
| 11-15 01:31 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-15 01:31 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-15 01:31 | +10 | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-15 01:31 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-15 01:31 | +10 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 01:31 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
