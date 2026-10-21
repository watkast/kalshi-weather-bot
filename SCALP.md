# Range-Scalp Bot

*Updated Wed Oct 21 11:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27146 | 23642 | 3504 (39) | 4 | $-7868.42 | -4.6% |
| **+10¢** | 20412 | 16364 | 4048 (55) | 6 | $-6948.59 | -5.4% |
| **+15¢** | 17091 | 12733 | 4358 (78) | 6 | $-6219.74 | -5.8% |
| **+20¢** | 15133 | 10566 | 4567 (98) | 6 | $-5568.49 | -5.9% |
| **+10¢ (15¢ stop)** | 33303 | 33244 | 59 (32) | 0 | $-12315.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 11:39 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-21 11:37 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-21 11:37 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-21 11:36 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-21 11:36 | +10 stop | XRP | DOWN | 0.71 | 0.55 | -1.93 |
| 10-21 11:35 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 11:35 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-21 11:34 | +10 stop | BTC | DOWN | 0.56 | 0.77 | 1.79 |
| 10-21 11:34 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-21 11:33 | +10 stop | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 10-21 11:33 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-21 11:33 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-21 11:33 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 10-21 11:33 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-21 11:33 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 11:33 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 10-21 11:33 | +5 | SOL | UP | 0.57 | open |  |
| 10-21 11:32 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-21 11:32 | +5 | XRP | UP | 0.54 | open |  |
| 10-21 11:32 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-21 11:32 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 10-21 11:32 | +20 | ZEC | UP | 0.64 | open |  |
| 10-21 11:32 | +15 | ZEC | UP | 0.64 | open |  |
| 10-21 11:32 | +10 | ZEC | UP | 0.64 | open |  |
| 10-21 11:32 | +5 | ZEC | UP | 0.64 | open |  |
| 10-21 11:32 | +10 stop | HYPE | DOWN | 0.38 | 0.57 | 1.55 |
| 10-21 11:32 | +20 | HYPE | DOWN | 0.38 | 0.58 | 1.65 |
| 10-21 11:32 | +15 | HYPE | DOWN | 0.38 | 0.57 | 1.55 |
| 10-21 11:32 | +10 | HYPE | DOWN | 0.38 | 0.57 | 1.55 |
| 10-21 11:32 | +5 | HYPE | DOWN | 0.38 | 0.57 | 1.55 |
| 10-21 11:31 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-21 11:31 | +20 | BNB | DOWN | 0.68 | 0.88 | 1.76 |
| 10-21 11:31 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-21 11:31 | +10 | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-21 11:31 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 10-21 11:31 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-21 11:31 | +20 | NEAR | DOWN | 0.62 | 0.84 | 1.93 |
| 10-21 11:31 | +15 | NEAR | DOWN | 0.62 | 0.79 | 1.41 |
| 10-21 11:31 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-21 11:31 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
