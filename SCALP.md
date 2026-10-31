# Range-Scalp Bot

*Updated Sat Oct 31 19:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42659 | 37193 | 5466 (61) | 0 | $-12086.39 | -4.5% |
| **+10¢** | 31814 | 25489 | 6325 (83) | 0 | $-10871.65 | -5.4% |
| **+15¢** | 26612 | 19790 | 6822 (111) | 0 | $-9988.48 | -6.0% |
| **+20¢** | 23636 | 16487 | 7149 (143) | 0 | $-8863.55 | -6.0% |
| **+10¢ (15¢ stop)** | 52054 | 51971 | 83 (48) | 0 | $-19703.37 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 19:42 | +10 stop | BNB | UP | 0.71 | 0.90 | 1.69 |
| 10-31 19:41 | +10 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +5 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +10 stop | SOL | DOWN | 0.70 | 0.30 | -4.30 |
| 10-31 19:41 | +15 | SOL | DOWN | 0.70 | 1.00 | 2.80 |
| 10-31 19:38 | +10 stop | HYPE | UP | 0.66 | 0.86 | 1.71 |
| 10-31 19:38 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 19:38 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.75 |
| 10-31 19:38 | +5 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 19:36 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 19:36 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.87 |
| 10-31 19:35 | +10 stop | BNB | UP | 0.67 | 0.49 | -2.14 |
| 10-31 19:35 | +10 stop | SOL | UP | 0.58 | 0.28 | -3.33 |
| 10-31 19:35 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:35 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 19:34 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 10-31 19:34 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-31 19:34 | +10 stop | HYPE | UP | 0.68 | 0.49 | -2.24 |
| 10-31 19:34 | +10 stop | ZEC | UP | 0.56 | 0.35 | -2.43 |
| 10-31 19:34 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 10-31 19:33 | +10 stop | XRP | UP | 0.65 | 0.38 | -3.03 |
| 10-31 19:33 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 19:33 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-31 19:33 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-31 19:33 | +5 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-31 19:33 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 10-31 19:33 | +20 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 10-31 19:33 | +15 | ZEC | DOWN | 0.71 | 0.91 | 1.76 |
| 10-31 19:33 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 19:33 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-31 19:32 | +10 stop | SOL | DOWN | 0.67 | 0.46 | -2.44 |
| 10-31 19:32 | +20 | SOL | DOWN | 0.66 | 1.00 | 3.19 |
| 10-31 19:32 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-31 19:32 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-31 19:32 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-31 19:32 | +5 | BNB | DOWN | 0.58 | yes | -5.98 |
| 10-31 19:31 | +10 stop | BNB | DOWN | 0.53 | 0.36 | -2.05 |
| 10-31 19:31 | +20 | BNB | DOWN | 0.53 | yes | -5.48 |
| 10-31 19:31 | +15 | BNB | DOWN | 0.53 | yes | -5.48 |
| 10-31 19:31 | +10 | BNB | DOWN | 0.53 | yes | -5.48 |
