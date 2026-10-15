# Range-Scalp Bot

*Updated Thu Oct 15 02:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16910 | 14674 | 2236 (28) | 4 | $-5194.32 | -4.9% |
| **+10¢** | 12786 | 10194 | 2592 (40) | 6 | $-4722.94 | -5.9% |
| **+15¢** | 10741 | 7953 | 2788 (59) | 7 | $-4247.44 | -6.3% |
| **+20¢** | 9540 | 6618 | 2922 (76) | 8 | $-3759.52 | -6.3% |
| **+10¢ (15¢ stop)** | 20818 | 20768 | 50 (29) | 3 | $-8046.90 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 02:08 | +10 stop | DOGE | UP | 0.58 | open |  |
| 10-15 02:08 | +5 | DOGE | UP | 0.58 | open |  |
| 10-15 02:08 | +10 stop | ETH | UP | 0.59 | open |  |
| 10-15 02:08 | +5 | ETH | UP | 0.59 | open |  |
| 10-15 02:08 | +10 stop | SOL | UP | 0.51 | open |  |
| 10-15 02:08 | +10 | SOL | UP | 0.51 | open |  |
| 10-15 02:08 | +5 | SOL | UP | 0.52 | open |  |
| 10-15 02:08 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 02:08 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-15 02:08 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-15 02:08 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-15 02:08 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 10-15 02:08 | +10 stop | HYPE | UP | 0.45 | 0.27 | -2.12 |
| 10-15 02:08 | +20 | HYPE | UP | 0.45 | open |  |
| 10-15 02:08 | +15 | HYPE | UP | 0.45 | open |  |
| 10-15 02:08 | +10 | HYPE | UP | 0.46 | open |  |
| 10-15 02:08 | +5 | HYPE | UP | 0.44 | 0.53 | 0.50 |
| 10-15 02:06 | +10 stop | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 10-15 02:06 | +5 | ETH | DOWN | 0.49 | 0.57 | 0.44 |
| 10-15 02:06 | +10 stop | ZEC | UP | 0.55 | 0.68 | 0.94 |
| 10-15 02:06 | +5 | ZEC | UP | 0.62 | 0.68 | 0.24 |
| 10-15 02:06 | +10 stop | XRP | UP | 0.62 | 0.44 | -2.15 |
| 10-15 02:06 | +15 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 10-15 02:06 | +10 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 10-15 02:06 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 10-15 02:06 | +5 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-15 02:05 | +10 stop | SOL | DOWN | 0.47 | 0.59 | 0.85 |
| 10-15 02:05 | +15 | SOL | DOWN | 0.47 | open |  |
| 10-15 02:05 | +10 | SOL | DOWN | 0.49 | 0.59 | 0.65 |
| 10-15 02:05 | +5 | SOL | DOWN | 0.49 | 0.55 | 0.24 |
| 10-15 02:05 | +10 stop | DOGE | DOWN | 0.48 | 0.31 | -2.03 |
| 10-15 02:05 | +15 | DOGE | DOWN | 0.48 | open |  |
| 10-15 02:05 | +10 | DOGE | DOWN | 0.48 | open |  |
| 10-15 02:05 | +5 | DOGE | DOWN | 0.48 | 0.54 | 0.24 |
| 10-15 02:05 | +5 | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-15 02:03 | +5 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-15 02:03 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 10-15 02:03 | +20 | NEAR | UP | 0.58 | 0.80 | 1.90 |
| 10-15 02:03 | +15 | NEAR | UP | 0.58 | 0.75 | 1.38 |
| 10-15 02:03 | +10 | NEAR | UP | 0.58 | 0.70 | 0.87 |
