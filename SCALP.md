# Range-Scalp Bot

*Updated Tue Oct 20 22:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26311 | 22914 | 3397 (32) | 2 | $-7694.03 | -4.6% |
| **+10¢** | 19797 | 15875 | 3922 (47) | 3 | $-6777.74 | -5.4% |
| **+15¢** | 16570 | 12350 | 4220 (71) | 2 | $-6047.12 | -5.8% |
| **+20¢** | 14659 | 10235 | 4424 (90) | 4 | $-5441.81 | -5.9% |
| **+10¢ (15¢ stop)** | 32216 | 32163 | 53 (30) | 1 | $-11766.67 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 22:25 | +10 | ZEC | UP | 0.57 | open |  |
| 10-20 22:25 | +10 stop | ZEC | UP | 0.65 | 0.49 | -1.94 |
| 10-20 22:25 | +5 | ZEC | UP | 0.65 | open |  |
| 10-20 22:25 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-20 22:24 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-20 22:24 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-20 22:24 | +10 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-20 22:24 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
| 10-20 22:23 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-20 22:23 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-20 22:23 | +10 stop | ETH | UP | 0.71 | 0.82 | 0.84 |
| 10-20 22:23 | +20 | ETH | UP | 0.71 | open |  |
| 10-20 22:23 | +15 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 10-20 22:23 | +10 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 10-20 22:23 | +5 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 10-20 22:23 | +10 stop | NEAR | UP | 0.65 | 0.48 | -2.04 |
| 10-20 22:23 | +15 | NEAR | UP | 0.65 | open |  |
| 10-20 22:22 | +5 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-20 22:22 | +10 stop | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 22:22 | +5 | ZEC | DOWN | 0.57 | 0.63 | 0.24 |
| 10-20 22:21 | +5 | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-20 22:21 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 10-20 22:21 | +10 stop | NEAR | DOWN | 0.57 | 0.27 | -3.32 |
| 10-20 22:20 | +5 | BNB | UP | 0.58 | 0.66 | 0.46 |
| 10-20 22:20 | +10 stop | SOL | UP | 0.63 | 0.83 | 1.73 |
| 10-20 22:20 | +15 | SOL | UP | 0.63 | 0.83 | 1.73 |
| 10-20 22:20 | +10 | SOL | UP | 0.63 | 0.83 | 1.73 |
| 10-20 22:20 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-20 22:20 | +10 stop | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 10-20 22:20 | +10 | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 10-20 22:20 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 10-20 22:20 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 10-20 22:20 | +10 | BTC | DOWN | 0.55 | open |  |
| 10-20 22:20 | +5 | BTC | DOWN | 0.55 | 0.60 | 0.15 |
| 10-20 22:20 | +10 stop | BNB | UP | 0.58 | 0.78 | 1.69 |
| 10-20 22:20 | +20 | BNB | UP | 0.57 | 0.78 | 1.79 |
| 10-20 22:20 | +15 | BNB | UP | 0.57 | 0.78 | 1.79 |
| 10-20 22:20 | +10 | BNB | UP | 0.57 | 0.78 | 1.79 |
| 10-20 22:20 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 10-20 22:20 | +10 stop | ETH | UP | 0.58 | 0.75 | 1.38 |
