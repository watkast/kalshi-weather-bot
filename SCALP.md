# Range-Scalp Bot

*Updated Sat Oct 31 19:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42643 | 37180 | 5463 (61) | 0 | $-12078.89 | -4.5% |
| **+10¢** | 31800 | 25478 | 6322 (83) | 0 | $-10866.48 | -5.4% |
| **+15¢** | 26598 | 19780 | 6818 (111) | 2 | $-9980.47 | -6.0% |
| **+20¢** | 23622 | 16477 | 7145 (143) | 4 | $-8859.76 | -6.0% |
| **+10¢ (15¢ stop)** | 52027 | 51944 | 83 (48) | 0 | $-19680.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 19:16 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-31 19:16 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +10 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 19:16 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-31 19:16 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-31 19:16 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-31 19:16 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 19:16 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 19:16 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-31 19:16 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-31 19:16 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-31 19:16 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-31 19:16 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:16 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-31 19:16 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-31 19:16 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:16 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:08 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-31 19:08 | +10 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-31 19:08 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-31 19:08 | +20 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-31 19:04 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.74 |
| 10-31 19:04 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-31 19:04 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:04 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-31 19:04 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-31 19:04 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-31 19:04 | +10 stop | HYPE | UP | 0.62 | 0.18 | -4.68 |
| 10-31 19:03 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-31 19:03 | +5 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 10-31 19:03 | +10 stop | ETH | UP | 0.59 | 0.79 | 1.71 |
| 10-31 19:03 | +20 | ETH | UP | 0.59 | 0.79 | 1.71 |
| 10-31 19:03 | +15 | ETH | UP | 0.59 | 0.79 | 1.71 |
| 10-31 19:03 | +10 | ETH | UP | 0.59 | 0.79 | 1.71 |
| 10-31 19:03 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
| 10-31 19:02 | +10 stop | ZEC | DOWN | 0.51 | 0.35 | -1.94 |
| 10-31 19:01 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.81 |
