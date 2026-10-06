# Range-Scalp Bot

*Updated Tue Oct 06 07:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4720 | 4079 | 641 (7) | 3 | $-1526.16 | -5.1% |
| **+10¢** | 3627 | 2880 | 747 (11) | 3 | $-1416.53 | -6.2% |
| **+15¢** | 3046 | 2258 | 788 (14) | 3 | $-1205.69 | -6.3% |
| **+20¢** | 2729 | 1908 | 821 (19) | 5 | $-997.22 | -5.8% |
| **+10¢ (15¢ stop)** | 5779 | 5766 | 13 (8) | 3 | $-2093.02 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 07:32 | +10 stop | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-06 07:32 | +20 | SOL | DOWN | 0.43 | open |  |
| 10-06 07:32 | +15 | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-06 07:32 | +10 | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-06 07:32 | +5 | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-06 07:32 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 10-06 07:32 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-06 07:32 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-06 07:32 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-06 07:32 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-06 07:32 | +10 stop | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 10-06 07:32 | +20 | ETH | DOWN | 0.45 | open |  |
| 10-06 07:32 | +15 | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 10-06 07:32 | +10 | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 10-06 07:32 | +5 | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 10-06 07:31 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 10-06 07:31 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-06 07:31 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-06 07:31 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-06 07:31 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-06 07:30 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-06 07:30 | +20 | ZEC | UP | 0.66 | open |  |
| 10-06 07:30 | +15 | ZEC | UP | 0.66 | open |  |
| 10-06 07:30 | +10 | ZEC | UP | 0.66 | open |  |
| 10-06 07:30 | +5 | ZEC | UP | 0.66 | open |  |
| 10-06 07:29 | +10 stop | ETH | DOWN | 0.34 | 0.56 | 1.86 |
| 10-06 07:24 | +10 stop | BNB | UP | 0.60 | 0.36 | -2.73 |
| 10-06 07:24 | +10 | BNB | UP | 0.60 | no | -6.15 |
| 10-06 07:24 | +10 stop | SOL | DOWN | 0.54 | 0.31 | -2.62 |
| 10-06 07:24 | +10 stop | ETH | UP | 0.62 | 0.39 | -2.64 |
| 10-06 07:24 | +5 | BNB | UP | 0.69 | no | -7.05 |
| 10-06 07:23 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-06 07:23 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-06 07:23 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 10-06 07:23 | +15 | BNB | UP | 0.57 | no | -5.88 |
| 10-06 07:23 | +10 | BNB | UP | 0.57 | 0.68 | 0.76 |
| 10-06 07:23 | +5 | BNB | UP | 0.57 | 0.64 | 0.35 |
| 10-06 07:22 | +10 stop | SOL | UP | 0.65 | 0.38 | -3.03 |
| 10-06 07:22 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.80 |
| 10-06 07:22 | +10 stop | ETH | DOWN | 0.58 | 0.37 | -2.45 |
