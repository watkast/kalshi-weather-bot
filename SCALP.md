# Range-Scalp Bot

*Updated Thu Oct 22 01:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28065 | 24451 | 3614 (39) | 0 | $-8089.42 | -4.6% |
| **+10¢** | 21085 | 16910 | 4175 (55) | 1 | $-7134.01 | -5.4% |
| **+15¢** | 17665 | 13173 | 4492 (78) | 0 | $-6354.02 | -5.7% |
| **+20¢** | 15635 | 10927 | 4708 (98) | 0 | $-5696.43 | -5.8% |
| **+10¢ (15¢ stop)** | 34464 | 34405 | 59 (32) | 0 | $-12887.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 01:51 | +10 stop | NEAR | UP | 0.59 | 0.40 | -2.24 |
| 10-22 01:51 | +10 stop | XRP | UP | 0.54 | 0.37 | -2.05 |
| 10-22 01:51 | +10 stop | BNB | UP | 0.70 | 0.42 | -3.13 |
| 10-22 01:51 | +10 stop | SOL | UP | 0.64 | 0.40 | -2.74 |
| 10-22 01:51 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-22 01:51 | +15 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-22 01:51 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-22 01:51 | +5 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-22 01:51 | +10 stop | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-22 01:51 | +20 | DOGE | DOWN | 0.55 | 0.86 | 2.83 |
| 10-22 01:51 | +15 | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-22 01:51 | +10 | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-22 01:51 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 10-22 01:51 | +10 stop | HYPE | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 01:51 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-22 01:51 | +10 | HYPE | DOWN | 0.63 | 0.82 | 1.58 |
| 10-22 01:51 | +5 | HYPE | DOWN | 0.63 | 0.72 | 0.54 |
| 10-22 01:50 | +20 | BNB | DOWN | 0.56 | 0.82 | 2.31 |
| 10-22 01:50 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-22 01:50 | +10 stop | NEAR | DOWN | 0.71 | 0.45 | -2.93 |
| 10-22 01:50 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-22 01:49 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 10-22 01:49 | +10 stop | XRP | DOWN | 0.69 | 0.43 | -2.93 |
| 10-22 01:49 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-22 01:49 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.53 |
| 10-22 01:49 | +10 stop | BNB | DOWN | 0.71 | 0.53 | -2.13 |
| 10-22 01:49 | +10 stop | ZEC | UP | 0.58 | 0.75 | 1.35 |
| 10-22 01:49 | +20 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 10-22 01:49 | +15 | ZEC | UP | 0.59 | 0.75 | 1.29 |
| 10-22 01:49 | +10 | ZEC | UP | 0.59 | 0.75 | 1.29 |
| 10-22 01:49 | +5 | ZEC | UP | 0.57 | 0.65 | 0.43 |
| 10-22 01:48 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-22 01:48 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-22 01:48 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.74 |
| 10-22 01:48 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.78 |
| 10-22 01:48 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-22 01:48 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.74 |
| 10-22 01:48 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.33 |
| 10-22 01:48 | +10 stop | BNB | UP | 0.49 | 0.61 | 0.85 |
| 10-22 01:48 | +15 | BNB | UP | 0.48 | 0.67 | 1.56 |
