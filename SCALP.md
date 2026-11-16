# Range-Scalp Bot

*Updated Mon Nov 16 22:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62388 | 54429 | 7959 (117) | 0 | $-16887.38 | -4.3% |
| **+10¢** | 46592 | 37279 | 9313 (159) | 0 | $-15763.23 | -5.4% |
| **+15¢** | 39042 | 28996 | 10046 (201) | 1 | $-14341.55 | -5.9% |
| **+20¢** | 34795 | 24259 | 10536 (256) | 1 | $-12534.55 | -5.7% |
| **+10¢ (15¢ stop)** | 75934 | 75778 | 156 (92) | 1 | $-28017.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 22:50 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 11-16 22:50 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 22:50 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-16 22:50 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 22:50 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 11-16 22:49 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 11-16 22:48 | +10 stop | HYPE | UP | 0.62 | 0.44 | -2.15 |
| 11-16 22:48 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-16 22:48 | +10 | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-16 22:48 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 22:47 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 22:47 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-16 22:47 | +15 | ZEC | UP | 0.69 | open |  |
| 11-16 22:47 | +10 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-16 22:47 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 11-16 22:47 | +5 | SOL | DOWN | 0.66 | 0.74 | 0.50 |
| 11-16 22:47 | +10 stop | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 22:47 | +20 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 11-16 22:47 | +15 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 22:47 | +10 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 22:47 | +5 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 22:46 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-16 22:46 | +20 | DOGE | DOWN | 0.62 | 0.85 | 2.04 |
| 11-16 22:46 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-16 22:46 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-16 22:46 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-16 22:46 | +10 stop | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 11-16 22:46 | +20 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 11-16 22:46 | +15 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 11-16 22:46 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 11-16 22:46 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 11-16 22:46 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-16 22:46 | +20 | BTC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-16 22:46 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-16 22:46 | +10 | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-16 22:46 | +5 | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-16 22:46 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 22:46 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 11-16 22:46 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 11-16 22:46 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
