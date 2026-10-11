# Range-Scalp Bot

*Updated Sun Oct 11 18:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12320 | 10626 | 1694 (25) | 0 | $-4113.74 | -5.3% |
| **+10¢** | 9358 | 7398 | 1960 (37) | 0 | $-3862.41 | -6.6% |
| **+15¢** | 7884 | 5803 | 2081 (54) | 0 | $-3295.97 | -6.7% |
| **+20¢** | 7029 | 4860 | 2169 (68) | 0 | $-2788.65 | -6.3% |
| **+10¢ (15¢ stop)** | 15190 | 15149 | 41 (25) | 0 | $-5998.02 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 18:42 | +10 stop | HYPE | UP | 0.45 | 0.57 | 0.84 |
| 10-11 18:41 | +10 | NEAR | UP | 0.65 | no | -6.66 |
| 10-11 18:41 | +10 stop | ETH | UP | 0.39 | 0.54 | 1.15 |
| 10-11 18:41 | +20 | ETH | UP | 0.39 | no | -4.07 |
| 10-11 18:41 | +15 | ETH | UP | 0.39 | 0.54 | 1.15 |
| 10-11 18:41 | +10 | ETH | UP | 0.39 | 0.54 | 1.15 |
| 10-11 18:41 | +5 | NEAR | UP | 0.65 | no | -6.66 |
| 10-11 18:41 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.99 |
| 10-11 18:41 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-11 18:41 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-11 18:41 | +5 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-11 18:41 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-11 18:41 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 10-11 18:41 | +20 | BTC | UP | 0.62 | no | -6.37 |
| 10-11 18:41 | +15 | BTC | UP | 0.62 | no | -6.37 |
| 10-11 18:41 | +10 | BTC | UP | 0.61 | no | -6.27 |
| 10-11 18:41 | +5 | BTC | UP | 0.61 | no | -6.27 |
| 10-11 18:40 | +10 stop | HYPE | DOWN | 0.58 | 0.40 | -2.15 |
| 10-11 18:40 | +20 | HYPE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-11 18:40 | +15 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-11 18:40 | +10 | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 10-11 18:40 | +5 | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 10-11 18:40 | +5 | NEAR | UP | 0.54 | 0.63 | 0.55 |
| 10-11 18:39 | +10 stop | NEAR | UP | 0.55 | 0.10 | -4.75 |
| 10-11 18:39 | +15 | NEAR | UP | 0.55 | no | -5.68 |
| 10-11 18:39 | +10 | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 10-11 18:39 | +5 | NEAR | UP | 0.54 | 0.60 | 0.25 |
| 10-11 18:39 | +10 stop | BNB | DOWN | 0.57 | 0.22 | -3.81 |
| 10-11 18:39 | +10 stop | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-11 18:38 | +10 stop | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-11 18:38 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-11 18:38 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 10-11 18:38 | +10 | SOL | UP | 0.54 | 0.67 | 0.96 |
| 10-11 18:38 | +5 | SOL | UP | 0.54 | 0.67 | 0.96 |
| 10-11 18:37 | +10 stop | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-11 18:37 | +10 stop | ETH | UP | 0.67 | 0.50 | -2.04 |
| 10-11 18:37 | +5 | ETH | UP | 0.67 | no | -6.86 |
| 10-11 18:37 | +5 | SOL | UP | 0.66 | 0.75 | 0.57 |
| 10-11 18:36 | +10 stop | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-11 18:36 | +20 | XRP | DOWN | 0.71 | 0.91 | 1.82 |
