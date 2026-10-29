# Range-Scalp Bot

*Updated Thu Oct 29 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38836 | 33895 | 4941 (49) | 1 | $-10866.10 | -4.4% |
| **+10¢** | 28973 | 23267 | 5706 (71) | 0 | $-9618.11 | -5.3% |
| **+15¢** | 24238 | 18107 | 6131 (97) | 0 | $-8563.91 | -5.6% |
| **+20¢** | 21506 | 15084 | 6422 (125) | 1 | $-7464.42 | -5.5% |
| **+10¢ (15¢ stop)** | 47502 | 47435 | 67 (35) | 0 | $-18021.26 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 02:35 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.62 |
| 10-29 02:35 | +5 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 10-29 02:35 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-29 02:35 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-29 02:35 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.31 |
| 10-29 02:35 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 02:35 | +10 stop | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 10-29 02:34 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 10-29 02:34 | +10 stop | DOGE | UP | 0.54 | 0.37 | -2.05 |
| 10-29 02:33 | +5 | NEAR | UP | 0.61 | open |  |
| 10-29 02:33 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.09 |
| 10-29 02:33 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.82 |
| 10-29 02:33 | +15 | ZEC | DOWN | 0.63 | 0.82 | 1.62 |
| 10-29 02:33 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 02:33 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 02:33 | +10 stop | NEAR | DOWN | 0.43 | 0.57 | 0.99 |
| 10-29 02:33 | +20 | NEAR | DOWN | 0.44 | 0.66 | 1.83 |
| 10-29 02:33 | +15 | NEAR | DOWN | 0.44 | 0.61 | 1.32 |
| 10-29 02:33 | +10 | NEAR | DOWN | 0.44 | 0.57 | 0.91 |
| 10-29 02:33 | +5 | NEAR | DOWN | 0.45 | 0.52 | 0.39 |
| 10-29 02:33 | +10 stop | DOGE | DOWN | 0.45 | 0.56 | 0.74 |
| 10-29 02:33 | +10 stop | HYPE | DOWN | 0.49 | 0.66 | 1.32 |
| 10-29 02:33 | +10 stop | ETH | DOWN | 0.48 | 0.61 | 0.95 |
| 10-29 02:33 | +10 | ETH | DOWN | 0.48 | 0.61 | 0.95 |
| 10-29 02:33 | +5 | ETH | DOWN | 0.48 | 0.54 | 0.24 |
| 10-29 02:32 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 02:32 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 10-29 02:32 | +15 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-29 02:32 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-29 02:32 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 10-29 02:32 | +10 stop | SOL | DOWN | 0.66 | 0.45 | -2.44 |
| 10-29 02:32 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-29 02:32 | +5 | SOL | DOWN | 0.66 | 0.74 | 0.50 |
| 10-29 02:31 | +10 stop | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-29 02:31 | +20 | ETH | DOWN | 0.53 | 0.76 | 1.99 |
| 10-29 02:31 | +15 | ETH | DOWN | 0.53 | 0.70 | 1.37 |
| 10-29 02:31 | +10 | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-29 02:31 | +5 | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-29 02:31 | +10 stop | SOL | DOWN | 0.55 | 0.69 | 1.07 |
| 10-29 02:31 | +20 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
