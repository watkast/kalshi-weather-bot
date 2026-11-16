# Range-Scalp Bot

*Updated Mon Nov 16 09:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61842 | 53948 | 7894 (115) | 0 | $-16764.49 | -4.3% |
| **+10¢** | 46200 | 36958 | 9242 (157) | 0 | $-15661.36 | -5.4% |
| **+15¢** | 38717 | 28751 | 9966 (196) | 0 | $-14261.50 | -5.9% |
| **+20¢** | 34519 | 24068 | 10451 (249) | 0 | $-12460.43 | -5.8% |
| **+10¢ (15¢ stop)** | 75286 | 75132 | 154 (90) | 0 | $-27763.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 09:49 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-16 09:46 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 09:46 | +20 | ETH | DOWN | 0.71 | 0.93 | 1.96 |
| 11-16 09:46 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 11-16 09:46 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 09:46 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 09:46 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 09:46 | +20 | BNB | DOWN | 0.65 | 0.92 | 2.43 |
| 11-16 09:46 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-16 09:46 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 09:46 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 09:46 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-16 09:46 | +20 | BTC | DOWN | 0.60 | 0.83 | 2.03 |
| 11-16 09:46 | +15 | BTC | DOWN | 0.60 | 0.83 | 2.03 |
| 11-16 09:46 | +10 | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-16 09:46 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 09:46 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 09:46 | +20 | HYPE | DOWN | 0.61 | 0.86 | 2.24 |
| 11-16 09:46 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-16 09:46 | +10 | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 09:46 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-16 09:42 | +10 stop | BTC | DOWN | 0.56 | 0.09 | -4.97 |
| 11-16 09:42 | +5 | BTC | DOWN | 0.56 | yes | -5.78 |
| 11-16 09:41 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 11-16 09:41 | +20 | BNB | DOWN | 0.63 | yes | -6.47 |
| 11-16 09:41 | +15 | BNB | DOWN | 0.63 | yes | -6.47 |
| 11-16 09:41 | +10 | BNB | DOWN | 0.63 | yes | -6.47 |
| 11-16 09:41 | +5 | BNB | DOWN | 0.63 | yes | -6.47 |
| 11-16 09:41 | +10 stop | XRP | UP | 0.68 | 0.98 | 2.81 |
| 11-16 09:41 | +10 stop | XRP | DOWN | 0.35 | 0.60 | 2.17 |
| 11-16 09:40 | +10 stop | SOL | DOWN | 0.61 | 0.40 | -2.44 |
| 11-16 09:40 | +10 | SOL | DOWN | 0.61 | yes | -6.27 |
| 11-16 09:40 | +5 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-16 09:40 | +10 stop | NEAR | UP | 0.67 | 0.89 | 1.97 |
| 11-16 09:40 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-16 09:40 | +10 stop | XRP | DOWN | 0.68 | 0.53 | -1.84 |
| 11-16 09:40 | +10 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-16 09:40 | +5 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-16 09:39 | +10 stop | SOL | UP | 0.65 | 0.30 | -3.81 |
| 11-16 09:39 | +10 stop | BTC | UP | 0.49 | 0.60 | 0.75 |
