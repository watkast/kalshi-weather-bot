# Range-Scalp Bot

*Updated Mon Oct 12 21:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13965 | 12090 | 1875 (25) | 7 | $-4415.06 | -5.0% |
| **+10¢** | 10568 | 8386 | 2182 (37) | 7 | $-4158.84 | -6.3% |
| **+15¢** | 8880 | 6546 | 2334 (55) | 8 | $-3689.07 | -6.6% |
| **+20¢** | 7898 | 5467 | 2431 (70) | 8 | $-3145.86 | -6.3% |
| **+10¢ (15¢ stop)** | 17138 | 17091 | 47 (27) | 2 | $-6682.90 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 21:37 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-12 21:37 | +5 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-12 21:37 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-12 21:36 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-12 21:35 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-12 21:35 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-12 21:35 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-12 21:35 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-12 21:35 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-12 21:34 | +10 stop | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 21:34 | +10 stop | BNB | DOWN | 0.63 | 0.87 | 2.15 |
| 10-12 21:34 | +10 | BNB | DOWN | 0.63 | 0.87 | 2.15 |
| 10-12 21:34 | +10 stop | BTC | UP | 0.66 | 0.46 | -2.34 |
| 10-12 21:34 | +10 | BTC | UP | 0.66 | open |  |
| 10-12 21:34 | +10 stop | SOL | UP | 0.51 | 0.22 | -3.21 |
| 10-12 21:34 | +15 | SOL | UP | 0.51 | open |  |
| 10-12 21:34 | +10 | SOL | UP | 0.51 | open |  |
| 10-12 21:34 | +5 | SOL | UP | 0.51 | 0.57 | 0.24 |
| 10-12 21:34 | +10 stop | DOGE | UP | 0.59 | 0.36 | -2.64 |
| 10-12 21:34 | +15 | DOGE | UP | 0.59 | open |  |
| 10-12 21:34 | +10 | DOGE | UP | 0.59 | open |  |
| 10-12 21:34 | +5 | DOGE | UP | 0.59 | open |  |
| 10-12 21:33 | +10 stop | XRP | UP | 0.65 | 0.46 | -2.20 |
| 10-12 21:33 | +10 | XRP | UP | 0.65 | open |  |
| 10-12 21:33 | +5 | XRP | UP | 0.64 | open |  |
| 10-12 21:33 | +10 stop | ZEC | UP | 0.58 | 0.40 | -2.15 |
| 10-12 21:33 | +10 | ZEC | UP | 0.58 | open |  |
| 10-12 21:33 | +5 | ZEC | UP | 0.58 | open |  |
| 10-12 21:32 | +5 | BNB | UP | 0.70 | open |  |
| 10-12 21:32 | +5 | BTC | UP | 0.70 | open |  |
| 10-12 21:32 | +5 | ETH | UP | 0.64 | open |  |
| 10-12 21:32 | +10 stop | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-12 21:32 | +20 | HYPE | UP | 0.60 | 0.80 | 1.71 |
| 10-12 21:32 | +15 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-12 21:32 | +10 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-12 21:32 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-12 21:31 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 21:31 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-12 21:31 | +15 | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 10-12 21:31 | +10 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
