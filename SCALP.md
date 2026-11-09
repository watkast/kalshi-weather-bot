# Range-Scalp Bot

*Updated Mon Nov 09 23:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53994 | 47092 | 6902 (89) | 0 | $-14765.36 | -4.3% |
| **+10¢** | 40327 | 32275 | 8052 (117) | 0 | $-13736.39 | -5.4% |
| **+15¢** | 33799 | 25120 | 8679 (149) | 0 | $-12514.81 | -5.9% |
| **+20¢** | 30088 | 20985 | 9103 (195) | 0 | $-10964.17 | -5.8% |
| **+10¢ (15¢ stop)** | 65775 | 65665 | 110 (66) | 0 | $-24361.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 22:58 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-09 22:58 | +5 | NEAR | DOWN | 0.52 | 0.59 | 0.35 |
| 11-09 22:58 | +10 stop | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +20 | BTC | UP | 0.59 | 0.88 | 2.65 |
| 11-09 22:58 | +15 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +10 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +5 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-09 22:56 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 11-09 22:56 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 11-09 22:56 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-09 22:56 | +10 stop | ETH | UP | 0.69 | 0.92 | 2.08 |
| 11-09 22:55 | +10 stop | DOGE | UP | 0.26 | 0.57 | 2.78 |
| 11-09 22:54 | +5 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-09 22:54 | +10 stop | DOGE | UP | 0.63 | 0.46 | -2.05 |
| 11-09 22:54 | +5 | DOGE | UP | 0.63 | no | -6.47 |
| 11-09 22:53 | +10 stop | BTC | DOWN | 0.48 | 0.64 | 1.25 |
| 11-09 22:53 | +20 | BTC | DOWN | 0.47 | 0.82 | 3.21 |
| 11-09 22:53 | +15 | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 11-09 22:53 | +10 | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 11-09 22:53 | +5 | BTC | DOWN | 0.47 | 0.55 | 0.44 |
| 11-09 22:53 | +10 stop | SOL | UP | 0.68 | 0.28 | -4.31 |
| 11-09 22:53 | +15 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 22:53 | +10 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 22:53 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-09 22:53 | +5 | DOGE | DOWN | 0.35 | 0.62 | 2.37 |
| 11-09 22:52 | +10 stop | SOL | DOWN | 0.58 | 0.34 | -2.74 |
| 11-09 22:52 | +5 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 11-09 22:52 | +10 stop | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-09 22:51 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.13 |
| 11-09 22:50 | +10 stop | DOGE | DOWN | 0.57 | 0.35 | -2.54 |
| 11-09 22:50 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.95 |
| 11-09 22:50 | +15 | HYPE | UP | 0.60 | 0.80 | 1.71 |
| 11-09 22:50 | +10 | HYPE | UP | 0.60 | 0.80 | 1.71 |
| 11-09 22:50 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 11-09 22:50 | +10 stop | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-09 22:49 | +10 stop | SOL | UP | 0.53 | 0.32 | -2.44 |
| 11-09 22:49 | +10 | SOL | UP | 0.53 | 0.65 | 0.86 |
| 11-09 22:49 | +5 | SOL | UP | 0.53 | 0.60 | 0.35 |
| 11-09 22:49 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 11-09 22:49 | +10 stop | NEAR | UP | 0.55 | 0.69 | 1.07 |
