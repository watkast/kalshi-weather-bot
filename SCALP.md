# Range-Scalp Bot

*Updated Sun Nov 15 14:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60923 | 53154 | 7769 (112) | 3 | $-16469.16 | -4.3% |
| **+10¢** | 45512 | 36406 | 9106 (150) | 0 | $-15505.73 | -5.4% |
| **+15¢** | 38111 | 28291 | 9820 (188) | 1 | $-14175.77 | -5.9% |
| **+20¢** | 33966 | 23666 | 10300 (240) | 1 | $-12454.89 | -5.8% |
| **+10¢ (15¢ stop)** | 74151 | 74000 | 151 (89) | 0 | $-27284.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 14:39 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-15 14:39 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 11-15 14:39 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 14:39 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 14:39 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-15 14:39 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-15 14:39 | +5 | ZEC | UP | 0.61 | open |  |
| 11-15 14:39 | +5 | NEAR | DOWN | 0.68 | 0.87 | 1.66 |
| 11-15 14:39 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-15 14:38 | +10 stop | NEAR | DOWN | 0.62 | 0.87 | 2.25 |
| 11-15 14:38 | +10 stop | ZEC | UP | 0.57 | 0.17 | -4.28 |
| 11-15 14:38 | +5 | ZEC | UP | 0.56 | 0.64 | 0.45 |
| 11-15 14:37 | +10 stop | SOL | UP | 0.59 | 0.42 | -2.05 |
| 11-15 14:37 | +10 stop | NEAR | UP | 0.65 | 0.39 | -2.93 |
| 11-15 14:37 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 11-15 14:36 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 11-15 14:36 | +10 stop | DOGE | UP | 0.69 | 0.52 | -2.03 |
| 11-15 14:36 | +5 | ZEC | UP | 0.65 | 0.73 | 0.50 |
| 11-15 14:36 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.05 |
| 11-15 14:36 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-15 14:36 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 11-15 14:36 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 11-15 14:35 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-15 14:35 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-15 14:35 | +10 stop | XRP | UP | 0.48 | 0.23 | -2.81 |
| 11-15 14:34 | +5 | BNB | UP | 0.59 | open |  |
| 11-15 14:34 | +5 | BTC | UP | 0.65 | open |  |
| 11-15 14:34 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 11-15 14:34 | +10 stop | HYPE | UP | 0.70 | 0.51 | -2.23 |
| 11-15 14:34 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 11-15 14:33 | +10 stop | BNB | DOWN | 0.52 | 0.79 | 2.40 |
| 11-15 14:33 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 14:33 | +10 stop | DOGE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-15 14:33 | +10 stop | XRP | DOWN | 0.57 | 0.42 | -1.86 |
| 11-15 14:33 | +10 | XRP | DOWN | 0.57 | 0.76 | 1.59 |
| 11-15 14:33 | +5 | XRP | DOWN | 0.57 | 0.65 | 0.46 |
| 11-15 14:32 | +10 stop | HYPE | DOWN | 0.68 | 0.41 | -3.03 |
| 11-15 14:32 | +20 | HYPE | DOWN | 0.68 | 0.93 | 2.32 |
| 11-15 14:32 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.25 |
| 11-15 14:32 | +10 | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
