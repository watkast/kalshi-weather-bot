# Range-Scalp Bot

*Updated Sat Oct 10 10:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10291 | 8870 | 1421 (22) | 2 | $-3526.08 | -5.4% |
| **+10¢** | 7783 | 6129 | 1654 (34) | 3 | $-3375.02 | -6.9% |
| **+15¢** | 6569 | 4817 | 1752 (49) | 4 | $-2851.37 | -6.9% |
| **+20¢** | 5838 | 4014 | 1824 (63) | 4 | $-2424.80 | -6.6% |
| **+10¢ (15¢ stop)** | 12631 | 12594 | 37 (24) | 3 | $-4948.99 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 10:32 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 10-10 10:32 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-10 10:32 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-10 10:32 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-10 10:32 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-10 10:31 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:31 | +20 | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:31 | +15 | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:31 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:31 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:31 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 10:31 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-10 10:31 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-10 10:31 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.01 |
| 10-10 10:31 | +5 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 10:30 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 10-10 10:30 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-10 10:30 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-10 10:30 | +10 | BNB | DOWN | 0.62 | open |  |
| 10-10 10:30 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-10 10:23 | +10 stop | ZEC | UP | 0.46 | 0.58 | 0.84 |
| 10-10 10:23 | +20 | ZEC | UP | 0.46 | no | -4.78 |
| 10-10 10:23 | +15 | ZEC | UP | 0.46 | no | -4.78 |
| 10-10 10:23 | +10 | ZEC | UP | 0.46 | 0.58 | 0.84 |
| 10-10 10:23 | +5 | ZEC | UP | 0.46 | 0.58 | 0.84 |
| 10-10 10:22 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-10 10:22 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.82 |
| 10-10 10:22 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.74 |
| 10-10 10:21 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-10 10:21 | +5 | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-10 10:19 | +5 | DOGE | UP | 0.57 | no | -5.88 |
| 10-10 10:18 | +10 stop | BNB | UP | 0.69 | 0.52 | -2.03 |
| 10-10 10:18 | +10 | BNB | UP | 0.69 | no | -7.05 |
| 10-10 10:17 | +10 stop | ETH | DOWN | 0.50 | 0.62 | 0.87 |
| 10-10 10:17 | +20 | ETH | DOWN | 0.50 | 0.70 | 1.69 |
| 10-10 10:17 | +15 | ETH | DOWN | 0.49 | 0.70 | 1.74 |
| 10-10 10:17 | +10 | ETH | DOWN | 0.49 | 0.62 | 0.92 |
| 10-10 10:17 | +5 | ETH | DOWN | 0.49 | 0.55 | 0.24 |
| 10-10 10:17 | +5 | BNB | UP | 0.65 | 0.70 | 0.22 |
| 10-10 10:17 | +10 stop | SOL | UP | 0.55 | 0.39 | -1.95 |
