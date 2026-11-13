# Range-Scalp Bot

*Updated Fri Nov 13 17:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58378 | 50940 | 7438 (105) | 4 | $-15720.52 | -4.3% |
| **+10¢** | 43619 | 34923 | 8696 (139) | 5 | $-14667.67 | -5.3% |
| **+15¢** | 36560 | 27196 | 9364 (174) | 7 | $-13229.32 | -5.8% |
| **+20¢** | 32567 | 22734 | 9833 (225) | 7 | $-11628.57 | -5.7% |
| **+10¢ (15¢ stop)** | 71112 | 70978 | 134 (82) | 1 | $-26165.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 17:27 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 11-13 17:26 | +10 stop | BNB | DOWN | 0.71 | 0.54 | -2.03 |
| 11-13 17:26 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-13 17:26 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-13 17:26 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-13 17:26 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-13 17:26 | +10 stop | NEAR | UP | 0.45 | 0.62 | 1.35 |
| 11-13 17:25 | +10 stop | ETH | UP | 0.61 | 0.43 | -2.15 |
| 11-13 17:25 | +10 | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-13 17:25 | +5 | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-13 17:25 | +10 stop | DOGE | DOWN | 0.32 | 0.57 | 2.16 |
| 11-13 17:25 | +20 | DOGE | DOWN | 0.32 | 0.57 | 2.16 |
| 11-13 17:25 | +15 | DOGE | DOWN | 0.32 | 0.57 | 2.16 |
| 11-13 17:25 | +10 | DOGE | DOWN | 0.32 | 0.57 | 2.16 |
| 11-13 17:25 | +5 | DOGE | DOWN | 0.32 | 0.57 | 2.16 |
| 11-13 17:25 | +10 stop | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 11-13 17:25 | +10 | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 11-13 17:25 | +5 | ETH | DOWN | 0.44 | 0.65 | 1.76 |
| 11-13 17:24 | +10 stop | XRP | DOWN | 0.47 | 0.30 | -1.98 |
| 11-13 17:24 | +15 | XRP | DOWN | 0.46 | open |  |
| 11-13 17:24 | +10 | XRP | DOWN | 0.46 | open |  |
| 11-13 17:24 | +5 | XRP | DOWN | 0.46 | 0.54 | 0.44 |
| 11-13 17:23 | +10 stop | NEAR | DOWN | 0.71 | 0.49 | -2.53 |
| 11-13 17:23 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-13 17:23 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-13 17:23 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-13 17:23 | +10 stop | HYPE | UP | 0.67 | 0.82 | 1.21 |
| 11-13 17:22 | +10 stop | SOL | DOWN | 0.65 | 0.39 | -2.93 |
| 11-13 17:22 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-13 17:21 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-13 17:21 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-13 17:21 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-13 17:21 | +10 | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-13 17:21 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-13 17:20 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 11-13 17:19 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 11-13 17:19 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 11-13 17:19 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-13 17:18 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-13 17:17 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
