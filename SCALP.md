# Range-Scalp Bot

*Updated Tue Nov 17 18:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63151 | 55090 | 8061 (117) | 0 | $-17169.19 | -4.3% |
| **+10¢** | 47181 | 37748 | 9433 (159) | 0 | $-16033.18 | -5.4% |
| **+15¢** | 39552 | 29381 | 10171 (201) | 0 | $-14529.52 | -5.9% |
| **+20¢** | 35242 | 24569 | 10673 (256) | 0 | $-12761.46 | -5.8% |
| **+10¢ (15¢ stop)** | 76853 | 76697 | 156 (92) | 0 | $-28284.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 18:35 | +5 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 11-17 18:34 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 18:34 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 11-17 18:34 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 18:34 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 18:34 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 18:34 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-17 18:34 | +20 | DOGE | DOWN | 0.64 | 0.90 | 2.37 |
| 11-17 18:34 | +15 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-17 18:34 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 18:34 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 18:34 | +10 stop | SOL | DOWN | 0.49 | 0.74 | 2.18 |
| 11-17 18:34 | +20 | SOL | DOWN | 0.49 | 0.74 | 2.20 |
| 11-17 18:34 | +15 | SOL | DOWN | 0.50 | 0.74 | 2.11 |
| 11-17 18:34 | +10 | SOL | DOWN | 0.48 | 0.58 | 0.65 |
| 11-17 18:34 | +5 | SOL | DOWN | 0.48 | 0.55 | 0.35 |
| 11-17 18:34 | +10 stop | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-17 18:34 | +10 | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-17 18:34 | +5 | NEAR | DOWN | 0.53 | 0.61 | 0.45 |
| 11-17 18:31 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 18:31 | +20 | NEAR | DOWN | 0.70 | 0.92 | 1.95 |
| 11-17 18:31 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 11-17 18:31 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-17 18:31 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.70 |
| 11-17 18:21 | +10 stop | NEAR | UP | 0.60 | 0.79 | 1.62 |
| 11-17 18:20 | +10 stop | NEAR | DOWN | 0.60 | 0.29 | -3.42 |
| 11-17 18:19 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
| 11-17 18:18 | +10 stop | ETH | UP | 0.68 | 0.86 | 1.55 |
| 11-17 18:18 | +10 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 11-17 18:18 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-17 18:18 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 11-17 18:18 | +5 | XRP | UP | 0.59 | 0.74 | 1.19 |
| 11-17 18:17 | +10 stop | BNB | UP | 0.61 | 0.88 | 2.45 |
| 11-17 18:17 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-17 18:17 | +5 | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 11-17 18:17 | +10 stop | SOL | DOWN | 0.63 | 0.48 | -1.85 |
| 11-17 18:16 | +10 stop | HYPE | UP | 0.53 | 0.71 | 1.47 |
| 11-17 18:16 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 11-17 18:16 | +20 | ETH | UP | 0.57 | 0.86 | 2.63 |
| 11-17 18:16 | +15 | ETH | UP | 0.57 | 0.74 | 1.38 |
