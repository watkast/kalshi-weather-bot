# Range-Scalp Bot

*Updated Mon Nov 16 22:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62350 | 54394 | 7956 (117) | 1 | $-16888.02 | -4.3% |
| **+10¢** | 46565 | 37255 | 9310 (159) | 1 | $-15767.84 | -5.4% |
| **+15¢** | 39019 | 28976 | 10043 (201) | 1 | $-14350.39 | -5.9% |
| **+20¢** | 34775 | 24243 | 10532 (256) | 2 | $-12542.20 | -5.8% |
| **+10¢ (15¢ stop)** | 75888 | 75732 | 156 (92) | 0 | $-27995.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 22:20 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.49 |
| 11-16 22:20 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.54 |
| 11-16 22:20 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 11-16 22:19 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 22:19 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-16 22:19 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-16 22:19 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 22:19 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 22:19 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-16 22:19 | +10 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 22:19 | +5 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 22:18 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 22:18 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
| 11-16 22:17 | +10 stop | DOGE | DOWN | 0.53 | 0.67 | 1.06 |
| 11-16 22:17 | +20 | DOGE | DOWN | 0.53 | 0.78 | 2.19 |
| 11-16 22:17 | +15 | DOGE | DOWN | 0.53 | 0.69 | 1.27 |
| 11-16 22:17 | +10 | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-16 22:17 | +5 | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-16 22:17 | +10 stop | ETH | DOWN | 0.62 | 0.80 | 1.51 |
| 11-16 22:17 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-16 22:17 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-16 22:17 | +15 | NEAR | DOWN | 0.66 | 0.85 | 1.68 |
| 11-16 22:17 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-16 22:17 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 11-16 22:17 | +10 stop | BNB | DOWN | 0.57 | 0.74 | 1.38 |
| 11-16 22:17 | +20 | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 11-16 22:17 | +15 | BNB | DOWN | 0.57 | 0.74 | 1.38 |
| 11-16 22:17 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-16 22:17 | +5 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-16 22:17 | +10 stop | SOL | DOWN | 0.64 | 0.44 | -2.35 |
| 11-16 22:17 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 11-16 22:17 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 11-16 22:17 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-16 22:17 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 22:16 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 22:16 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-16 22:16 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 22:16 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 22:16 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-16 22:16 | +10 stop | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
