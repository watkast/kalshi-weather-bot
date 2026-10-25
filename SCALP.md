# Range-Scalp Bot

*Updated Sun Oct 25 02:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32432 | 28281 | 4151 (42) | 1 | $-9217.65 | -4.5% |
| **+10¢** | 24275 | 19467 | 4808 (60) | 3 | $-8259.85 | -5.4% |
| **+15¢** | 20326 | 15155 | 5171 (83) | 4 | $-7393.99 | -5.8% |
| **+20¢** | 18004 | 12593 | 5411 (105) | 4 | $-6539.76 | -5.8% |
| **+10¢ (15¢ stop)** | 39834 | 39774 | 60 (32) | 2 | $-15195.81 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 02:33 | +10 stop | HYPE | UP | 0.48 | open |  |
| 10-25 02:33 | +5 | HYPE | UP | 0.48 | 0.54 | 0.24 |
| 10-25 02:32 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 10-25 02:32 | +20 | ZEC | UP | 0.67 | open |  |
| 10-25 02:32 | +15 | ZEC | UP | 0.67 | open |  |
| 10-25 02:32 | +10 | ZEC | UP | 0.67 | open |  |
| 10-25 02:32 | +5 | ZEC | UP | 0.67 | open |  |
| 10-25 02:32 | +10 stop | DOGE | UP | 0.59 | 0.72 | 0.98 |
| 10-25 02:32 | +20 | DOGE | UP | 0.59 | open |  |
| 10-25 02:32 | +15 | DOGE | UP | 0.59 | open |  |
| 10-25 02:32 | +10 | DOGE | UP | 0.59 | 0.72 | 0.98 |
| 10-25 02:32 | +5 | DOGE | UP | 0.59 | 0.72 | 0.98 |
| 10-25 02:32 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-25 02:32 | +20 | SOL | UP | 0.64 | open |  |
| 10-25 02:32 | +15 | SOL | UP | 0.64 | open |  |
| 10-25 02:32 | +10 | SOL | UP | 0.64 | open |  |
| 10-25 02:32 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 10-25 02:32 | +10 stop | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 10-25 02:32 | +20 | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 10-25 02:32 | +15 | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 10-25 02:32 | +10 | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 10-25 02:32 | +5 | NEAR | UP | 0.52 | 0.58 | 0.24 |
| 10-25 02:32 | +10 stop | HYPE | UP | 0.54 | 0.65 | 0.76 |
| 10-25 02:32 | +20 | HYPE | UP | 0.54 | open |  |
| 10-25 02:32 | +15 | HYPE | UP | 0.54 | open |  |
| 10-25 02:32 | +10 | HYPE | UP | 0.56 | open |  |
| 10-25 02:32 | +5 | HYPE | UP | 0.56 | 0.65 | 0.56 |
| 10-25 02:28 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 10-25 02:28 | +20 | ETH | DOWN | 0.43 | yes | -4.48 |
| 10-25 02:28 | +15 | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 10-25 02:28 | +10 | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 10-25 02:28 | +5 | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 10-25 02:28 | +10 stop | ZEC | DOWN | 0.32 | 0.54 | 1.86 |
| 10-25 02:28 | +10 | ZEC | DOWN | 0.32 | 0.54 | 1.86 |
| 10-25 02:26 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-25 02:26 | +15 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-25 02:26 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-25 02:23 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-25 02:23 | +10 | ETH | DOWN | 0.63 | 0.79 | 1.33 |
| 10-25 02:23 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
