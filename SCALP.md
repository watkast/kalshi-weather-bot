# Range-Scalp Bot

*Updated Sun Oct 18 09:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22370 | 19475 | 2895 (29) | 4 | $-6502.61 | -4.6% |
| **+10¢** | 16839 | 13492 | 3347 (43) | 8 | $-5793.27 | -5.5% |
| **+15¢** | 14103 | 10490 | 3613 (63) | 8 | $-5305.53 | -6.0% |
| **+20¢** | 12480 | 8696 | 3784 (81) | 9 | $-4745.82 | -6.1% |
| **+10¢ (15¢ stop)** | 27525 | 27475 | 50 (29) | 3 | $-10528.64 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 09:48 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 10-18 09:48 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 10-18 09:48 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 10-18 09:48 | +10 stop | ZEC | UP | 0.57 | open |  |
| 10-18 09:48 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-18 09:48 | +20 | ETH | UP | 0.67 | open |  |
| 10-18 09:48 | +15 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 10-18 09:48 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-18 09:48 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 10-18 09:47 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-18 09:47 | +5 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-18 09:47 | +10 stop | DOGE | UP | 0.66 | open |  |
| 10-18 09:47 | +10 stop | BTC | UP | 0.68 | open |  |
| 10-18 09:47 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-18 09:47 | +10 stop | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-18 09:47 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-18 09:46 | +10 stop | BNB | DOWN | 0.60 | 0.42 | -2.15 |
| 10-18 09:46 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-18 09:46 | +15 | BNB | DOWN | 0.61 | open |  |
| 10-18 09:46 | +10 | BNB | DOWN | 0.61 | open |  |
| 10-18 09:46 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-18 09:46 | +10 stop | NEAR | DOWN | 0.57 | 0.37 | -2.35 |
| 10-18 09:46 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-18 09:46 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-18 09:46 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-18 09:46 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-18 09:46 | +10 stop | ZEC | DOWN | 0.56 | 0.40 | -1.95 |
| 10-18 09:46 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-18 09:46 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-18 09:46 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-18 09:46 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-18 09:46 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 10-18 09:46 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-18 09:46 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-18 09:46 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-18 09:46 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-18 09:46 | +10 stop | DOGE | DOWN | 0.65 | 0.47 | -2.14 |
| 10-18 09:46 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-18 09:46 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-18 09:46 | +10 | DOGE | DOWN | 0.65 | open |  |
