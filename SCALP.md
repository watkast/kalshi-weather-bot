# Range-Scalp Bot

*Updated Sat Oct 17 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21340 | 18585 | 2755 (29) | 0 | $-6156.84 | -4.6% |
| **+10¢** | 16046 | 12862 | 3184 (41) | 0 | $-5500.85 | -5.5% |
| **+15¢** | 13418 | 9987 | 3431 (61) | 0 | $-4991.16 | -5.9% |
| **+20¢** | 11889 | 8293 | 3596 (80) | 0 | $-4446.26 | -6.0% |
| **+10¢ (15¢ stop)** | 26198 | 26148 | 50 (29) | 0 | $-9994.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 17:38 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.95 |
| 10-17 17:38 | +5 | BTC | UP | 0.65 | 0.80 | 1.22 |
| 10-17 17:38 | +10 stop | DOGE | UP | 0.55 | 0.75 | 1.68 |
| 10-17 17:38 | +15 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 10-17 17:38 | +10 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-17 17:38 | +5 | ZEC | UP | 0.64 | 0.69 | 0.18 |
| 10-17 17:38 | +10 stop | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 17:38 | +5 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 17:38 | +10 stop | XRP | DOWN | 0.45 | 0.58 | 0.94 |
| 10-17 17:37 | +10 stop | ETH | UP | 0.71 | 0.87 | 1.37 |
| 10-17 17:37 | +10 stop | BTC | UP | 0.62 | 0.80 | 1.51 |
| 10-17 17:37 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-17 17:36 | +10 stop | BTC | DOWN | 0.58 | 0.41 | -2.05 |
| 10-17 17:36 | +10 stop | DOGE | DOWN | 0.64 | 0.44 | -2.35 |
| 10-17 17:36 | +10 stop | SOL | DOWN | 0.60 | 0.39 | -2.47 |
| 10-17 17:36 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-17 17:36 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 10-17 17:36 | +10 stop | ZEC | DOWN | 0.55 | 0.36 | -2.25 |
| 10-17 17:36 | +10 stop | NEAR | DOWN | 0.61 | 0.26 | -3.81 |
| 10-17 17:36 | +10 stop | ETH | DOWN | 0.64 | 0.47 | -2.05 |
| 10-17 17:35 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-17 17:35 | +10 | BNB | UP | 0.68 | 0.79 | 0.85 |
| 10-17 17:35 | +5 | BNB | UP | 0.68 | 0.79 | 0.85 |
| 10-17 17:35 | +10 stop | HYPE | DOWN | 0.69 | 0.50 | -2.23 |
| 10-17 17:34 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-17 17:34 | +5 | SOL | UP | 0.51 | 0.60 | 0.55 |
| 10-17 17:34 | +5 | NEAR | UP | 0.70 | 0.78 | 0.52 |
| 10-17 17:34 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-17 17:33 | +5 | SOL | UP | 0.56 | 0.64 | 0.45 |
| 10-17 17:33 | +10 stop | ZEC | UP | 0.61 | 0.41 | -2.34 |
| 10-17 17:33 | +10 | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 10-17 17:33 | +10 stop | DOGE | UP | 0.56 | 0.38 | -2.15 |
| 10-17 17:33 | +5 | SOL | UP | 0.57 | 0.63 | 0.25 |
| 10-17 17:32 | +10 stop | HYPE | DOWN | 0.64 | 0.46 | -2.15 |
| 10-17 17:32 | +20 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 10-17 17:32 | +15 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 10-17 17:32 | +10 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 10-17 17:32 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-17 17:31 | +10 stop | BNB | UP | 0.69 | 0.79 | 0.73 |
| 10-17 17:31 | +20 | BNB | UP | 0.69 | 0.91 | 1.99 |
