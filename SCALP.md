# Range-Scalp Bot

*Updated Sat Oct 31 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41725 | 36411 | 5314 (54) | 5 | $-11689.49 | -4.4% |
| **+10¢** | 31101 | 24952 | 6149 (78) | 5 | $-10425.19 | -5.3% |
| **+15¢** | 25993 | 19363 | 6630 (106) | 5 | $-9519.12 | -5.8% |
| **+20¢** | 23076 | 16132 | 6944 (137) | 5 | $-8387.21 | -5.8% |
| **+10¢ (15¢ stop)** | 50862 | 50787 | 75 (41) | 0 | $-19186.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 03:57 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 03:56 | +10 stop | BNB | UP | 0.41 | 0.58 | 1.35 |
| 10-31 03:56 | +10 stop | XRP | DOWN | 0.64 | 0.90 | 2.38 |
| 10-31 03:54 | +10 stop | DOGE | DOWN | 0.49 | 0.64 | 1.15 |
| 10-31 03:53 | +10 stop | DOGE | UP | 0.48 | 0.61 | 0.95 |
| 10-31 03:51 | +10 stop | BNB | DOWN | 0.58 | 0.41 | -2.05 |
| 10-31 03:50 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-31 03:50 | +10 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 03:50 | +5 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 03:50 | +10 stop | XRP | DOWN | 0.53 | 0.67 | 1.06 |
| 10-31 03:49 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 03:49 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-31 03:48 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-31 03:47 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-31 03:47 | +20 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 10-31 03:47 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-31 03:47 | +10 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-31 03:47 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 10-31 03:47 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-31 03:47 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-31 03:47 | +20 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-31 03:47 | +15 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-31 03:47 | +10 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-31 03:47 | +5 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-31 03:47 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 03:47 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-31 03:47 | +15 | ZEC | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 03:47 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 03:47 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-31 03:47 | +10 stop | DOGE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-31 03:47 | +20 | DOGE | DOWN | 0.54 | 0.84 | 2.72 |
| 10-31 03:47 | +15 | DOGE | DOWN | 0.54 | 0.84 | 2.72 |
| 10-31 03:47 | +10 | DOGE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-31 03:47 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-31 03:46 | +10 stop | BNB | UP | 0.55 | 0.40 | -1.85 |
| 10-31 03:46 | +20 | BNB | UP | 0.55 | open |  |
| 10-31 03:46 | +15 | BNB | UP | 0.55 | open |  |
| 10-31 03:46 | +10 | BNB | UP | 0.55 | open |  |
| 10-31 03:46 | +5 | BNB | UP | 0.55 | open |  |
| 10-31 03:46 | +10 stop | ETH | UP | 0.61 | 0.38 | -2.64 |
