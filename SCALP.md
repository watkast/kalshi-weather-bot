# Range-Scalp Bot

*Updated Sat Oct 17 22:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21668 | 18892 | 2776 (29) | 8 | $-6100.80 | -4.5% |
| **+10¢** | 16298 | 13086 | 3212 (41) | 8 | $-5423.25 | -5.3% |
| **+15¢** | 13628 | 10161 | 3467 (61) | 8 | $-4923.73 | -5.8% |
| **+20¢** | 12069 | 8435 | 3634 (80) | 8 | $-4377.21 | -5.8% |
| **+10¢ (15¢ stop)** | 26612 | 26562 | 50 (29) | 5 | $-10126.96 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 22:36 | +5 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 22:35 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-17 22:35 | +10 stop | ETH | UP | 0.57 | open |  |
| 10-17 22:35 | +10 stop | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 10-17 22:35 | +10 stop | XRP | DOWN | 0.50 | open |  |
| 10-17 22:34 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-17 22:34 | +10 stop | BTC | UP | 0.55 | 0.69 | 1.07 |
| 10-17 22:34 | +10 stop | SOL | DOWN | 0.55 | open |  |
| 10-17 22:34 | +10 | SOL | DOWN | 0.55 | open |  |
| 10-17 22:34 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 10-17 22:34 | +10 stop | XRP | DOWN | 0.52 | 0.68 | 1.26 |
| 10-17 22:34 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 10-17 22:33 | +10 stop | ETH | DOWN | 0.64 | 0.45 | -2.25 |
| 10-17 22:33 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-17 22:33 | +20 | HYPE | DOWN | 0.61 | 0.83 | 1.89 |
| 10-17 22:33 | +15 | HYPE | DOWN | 0.61 | 0.83 | 1.89 |
| 10-17 22:33 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.05 |
| 10-17 22:33 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.33 |
| 10-17 22:33 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-17 22:33 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-17 22:33 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-17 22:33 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-17 22:33 | +5 | ZEC | DOWN | 0.71 | open |  |
| 10-17 22:33 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-17 22:33 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-17 22:33 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-17 22:33 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-17 22:33 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-17 22:33 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-17 22:33 | +20 | SOL | DOWN | 0.58 | open |  |
| 10-17 22:33 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-17 22:33 | +10 | SOL | DOWN | 0.57 | 0.68 | 0.73 |
| 10-17 22:33 | +5 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-17 22:32 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 10-17 22:32 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-17 22:32 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-17 22:32 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-17 22:32 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-17 22:32 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-17 22:32 | +20 | DOGE | DOWN | 0.68 | open |  |
