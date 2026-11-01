# Range-Scalp Bot

*Updated Sun Nov 01 02:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43089 | 37558 | 5531 (62) | 3 | $-12255.42 | -4.5% |
| **+10¢** | 32131 | 25740 | 6391 (84) | 4 | $-10986.84 | -5.4% |
| **+15¢** | 26878 | 19990 | 6888 (112) | 5 | $-10064.93 | -6.0% |
| **+20¢** | 23871 | 16657 | 7214 (146) | 6 | $-8878.68 | -5.9% |
| **+10¢ (15¢ stop)** | 52548 | 52465 | 83 (48) | 3 | $-19897.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 02:31 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 02:31 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-01 02:31 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-01 02:31 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-01 02:31 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 11-01 02:31 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 02:31 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-01 02:31 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-01 02:31 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 02:31 | +5 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 02:31 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-01 02:31 | +20 | ETH | UP | 0.56 | open |  |
| 11-01 02:31 | +15 | ETH | UP | 0.56 | open |  |
| 11-01 02:31 | +10 | ETH | UP | 0.56 | open |  |
| 11-01 02:31 | +5 | ETH | UP | 0.56 | open |  |
| 11-01 02:31 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 11-01 02:31 | +20 | ZEC | UP | 0.64 | open |  |
| 11-01 02:31 | +15 | ZEC | UP | 0.64 | open |  |
| 11-01 02:31 | +10 | ZEC | UP | 0.64 | open |  |
| 11-01 02:31 | +5 | ZEC | UP | 0.64 | open |  |
| 11-01 02:31 | +10 stop | SOL | DOWN | 0.67 | open |  |
| 11-01 02:31 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-01 02:31 | +15 | SOL | DOWN | 0.66 | open |  |
| 11-01 02:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-01 02:31 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-01 02:31 | +10 stop | BNB | UP | 0.58 | open |  |
| 11-01 02:31 | +20 | BNB | UP | 0.58 | open |  |
| 11-01 02:31 | +15 | BNB | UP | 0.58 | open |  |
| 11-01 02:31 | +10 | BNB | UP | 0.58 | open |  |
| 11-01 02:31 | +5 | BNB | UP | 0.58 | open |  |
| 11-01 02:29 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-01 02:29 | +20 | DOGE | DOWN | 0.68 | no | 3.04 |
| 11-01 02:29 | +15 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-01 02:29 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 02:29 | +5 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 02:26 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-01 02:26 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 02:25 | +10 stop | SOL | UP | 0.67 | 0.34 | -3.62 |
| 11-01 02:25 | +10 | SOL | UP | 0.67 | no | -6.86 |
| 11-01 02:25 | +5 | SOL | UP | 0.67 | no | -6.86 |
