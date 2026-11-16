# Range-Scalp Bot

*Updated Mon Nov 16 20:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62171 | 54239 | 7932 (117) | 0 | $-16828.72 | -4.3% |
| **+10¢** | 46429 | 37148 | 9281 (159) | 0 | $-15696.16 | -5.4% |
| **+15¢** | 38903 | 28890 | 10013 (200) | 0 | $-14307.87 | -5.9% |
| **+20¢** | 34679 | 24179 | 10500 (255) | 0 | $-12484.05 | -5.7% |
| **+10¢ (15¢ stop)** | 75682 | 75526 | 156 (92) | 0 | $-27950.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 19:50 | +10 stop | DOGE | UP | 0.64 | 0.83 | 1.66 |
| 11-16 19:50 | +5 | DOGE | UP | 0.64 | 0.73 | 0.62 |
| 11-16 19:50 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-16 19:50 | +10 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-16 19:50 | +5 | XRP | UP | 0.68 | 0.75 | 0.40 |
| 11-16 19:50 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 11-16 19:50 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-16 19:50 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-16 19:50 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 11-16 19:49 | +10 stop | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-16 19:49 | +10 stop | HYPE | UP | 0.71 | 0.84 | 1.05 |
| 11-16 19:49 | +10 stop | BNB | UP | 0.60 | 0.71 | 0.78 |
| 11-16 19:49 | +10 stop | ETH | DOWN | 0.57 | 0.33 | -2.74 |
| 11-16 19:49 | +10 | ETH | DOWN | 0.57 | yes | -5.88 |
| 11-16 19:49 | +5 | ETH | DOWN | 0.57 | yes | -5.88 |
| 11-16 19:49 | +5 | DOGE | DOWN | 0.49 | 0.55 | 0.28 |
| 11-16 19:49 | +10 stop | NEAR | DOWN | 0.54 | 0.32 | -2.54 |
| 11-16 19:49 | +15 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-16 19:49 | +10 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-16 19:49 | +5 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-16 19:47 | +5 | BNB | DOWN | 0.69 | yes | -7.04 |
| 11-16 19:47 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-16 19:47 | +20 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +15 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +10 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +5 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +5 | BTC | DOWN | 0.71 | yes | -7.25 |
| 11-16 19:47 | +10 stop | HYPE | DOWN | 0.62 | 0.40 | -2.54 |
| 11-16 19:47 | +20 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +15 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:47 | +10 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-16 19:47 | +5 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 11-16 19:46 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.48 |
| 11-16 19:46 | +20 | DOGE | DOWN | 0.66 | yes | -6.80 |
| 11-16 19:46 | +15 | DOGE | DOWN | 0.66 | yes | -6.74 |
| 11-16 19:46 | +10 | DOGE | DOWN | 0.66 | yes | -6.80 |
| 11-16 19:46 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.36 |
| 11-16 19:46 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.95 |
| 11-16 19:46 | +20 | BNB | DOWN | 0.60 | yes | -6.17 |
| 11-16 19:46 | +15 | BNB | DOWN | 0.60 | yes | -6.17 |
