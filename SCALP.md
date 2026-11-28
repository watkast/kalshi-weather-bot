# Range-Scalp Bot

*Updated Sat Nov 28 12:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74684 | 65176 | 9508 (171) | 5 | $-19914.05 | -4.2% |
| **+10¢** | 55631 | 44526 | 11105 (217) | 7 | $-18535.94 | -5.3% |
| **+15¢** | 46575 | 34617 | 11958 (275) | 7 | $-16591.32 | -5.7% |
| **+20¢** | 41441 | 28850 | 12591 (343) | 8 | $-14993.57 | -5.8% |
| **+10¢ (15¢ stop)** | 90895 | 90675 | 220 (136) | 0 | $-33576.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 12:41 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-28 12:41 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-28 12:41 | +10 stop | DOGE | UP | 0.52 | 0.35 | -2.04 |
| 11-28 12:41 | +10 stop | SOL | UP | 0.67 | 0.49 | -2.14 |
| 11-28 12:41 | +10 stop | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-28 12:40 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-28 12:40 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-28 12:40 | +10 stop | SOL | DOWN | 0.62 | 0.44 | -2.15 |
| 11-28 12:39 | +10 stop | HYPE | UP | 0.58 | 0.72 | 1.07 |
| 11-28 12:39 | +20 | HYPE | UP | 0.58 | 0.78 | 1.69 |
| 11-28 12:39 | +15 | HYPE | UP | 0.58 | 0.77 | 1.59 |
| 11-28 12:39 | +10 | HYPE | UP | 0.58 | 0.72 | 1.07 |
| 11-28 12:39 | +5 | HYPE | UP | 0.58 | 0.72 | 1.07 |
| 11-28 12:38 | +10 stop | SOL | DOWN | 0.69 | 0.39 | -3.32 |
| 11-28 12:38 | +10 stop | BNB | DOWN | 0.67 | 0.35 | -3.52 |
| 11-28 12:37 | +5 | BNB | UP | 0.53 | 0.64 | 0.75 |
| 11-28 12:37 | +10 stop | BTC | UP | 0.42 | 0.54 | 0.84 |
| 11-28 12:37 | +10 stop | SOL | UP | 0.60 | 0.36 | -2.74 |
| 11-28 12:36 | +5 | BNB | UP | 0.58 | 0.69 | 0.77 |
| 11-28 12:36 | +10 stop | DOGE | DOWN | 0.50 | 0.65 | 1.16 |
| 11-28 12:35 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.95 |
| 11-28 12:35 | +10 stop | BTC | UP | 0.58 | 0.41 | -2.05 |
| 11-28 12:35 | +10 stop | SOL | UP | 0.69 | 0.47 | -2.53 |
| 11-28 12:34 | +10 stop | ZEC | DOWN | 0.56 | 0.69 | 0.97 |
| 11-28 12:34 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.08 |
| 11-28 12:34 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.35 |
| 11-28 12:34 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-28 12:34 | +10 stop | ETH | DOWN | 0.59 | 0.79 | 1.71 |
| 11-28 12:33 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 11-28 12:33 | +10 stop | BNB | UP | 0.61 | 0.42 | -2.25 |
| 11-28 12:33 | +20 | BNB | UP | 0.61 | open |  |
| 11-28 12:33 | +15 | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-28 12:33 | +10 | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-28 12:33 | +5 | BNB | UP | 0.61 | 0.66 | 0.17 |
| 11-28 12:33 | +10 stop | ETH | UP | 0.43 | 0.57 | 1.04 |
| 11-28 12:33 | +5 | BTC | UP | 0.68 | open |  |
| 11-28 12:32 | +5 | SOL | UP | 0.66 | open |  |
| 11-28 12:32 | +10 stop | NEAR | UP | 0.56 | 0.36 | -2.35 |
| 11-28 12:32 | +10 | NEAR | UP | 0.56 | open |  |
| 11-28 12:32 | +5 | NEAR | UP | 0.63 | open |  |
