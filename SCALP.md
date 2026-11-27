# Range-Scalp Bot

*Updated Fri Nov 27 08:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73562 | 64198 | 9364 (165) | 0 | $-19607.33 | -4.2% |
| **+10¢** | 54817 | 43881 | 10936 (210) | 0 | $-18243.86 | -5.3% |
| **+15¢** | 45906 | 34127 | 11779 (268) | 0 | $-16342.01 | -5.7% |
| **+20¢** | 40854 | 28450 | 12404 (334) | 0 | $-14752.75 | -5.8% |
| **+10¢ (15¢ stop)** | 89596 | 89384 | 212 (129) | 0 | $-33152.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 08:12 | +10 stop | ETH | UP | 0.60 | 0.96 | 3.36 |
| 11-27 08:11 | +10 stop | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-27 08:08 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-27 08:06 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 11-27 08:05 | +10 stop | ETH | UP | 0.71 | 0.89 | 1.58 |
| 11-27 08:03 | +10 stop | DOGE | UP | 0.69 | 0.84 | 1.25 |
| 11-27 08:03 | +10 stop | SOL | UP | 0.68 | 0.84 | 1.34 |
| 11-27 08:02 | +20 | DOGE | UP | 0.71 | 0.94 | 2.06 |
| 11-27 08:02 | +15 | DOGE | UP | 0.71 | 0.94 | 2.06 |
| 11-27 08:02 | +10 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-27 08:02 | +5 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-27 08:02 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-27 08:02 | +20 | BTC | UP | 0.62 | 0.86 | 2.14 |
| 11-27 08:02 | +15 | BTC | UP | 0.62 | 0.79 | 1.41 |
| 11-27 08:02 | +10 | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-27 08:02 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 11-27 08:01 | +5 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:01 | +10 stop | BNB | DOWN | 0.56 | 0.32 | -2.74 |
| 11-27 08:01 | +20 | BNB | DOWN | 0.55 | yes | -5.68 |
| 11-27 08:01 | +15 | BNB | DOWN | 0.55 | yes | -5.68 |
| 11-27 08:01 | +10 | BNB | DOWN | 0.55 | yes | -5.68 |
| 11-27 08:01 | +5 | BNB | DOWN | 0.55 | yes | -5.68 |
| 11-27 08:01 | +10 stop | ZEC | UP | 0.64 | 0.45 | -2.25 |
| 11-27 08:01 | +20 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 11-27 08:01 | +15 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 11-27 08:01 | +10 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 11-27 08:01 | +5 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 11-27 08:01 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 11-27 08:01 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 11-27 08:01 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-27 08:01 | +10 | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 11-27 08:01 | +5 | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 11-27 08:01 | +10 stop | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 11-27 08:01 | +20 | HYPE | UP | 0.69 | 0.90 | 1.92 |
| 11-27 08:01 | +15 | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 11-27 08:01 | +10 | HYPE | UP | 0.69 | 0.86 | 1.46 |
| 11-27 08:01 | +5 | HYPE | UP | 0.69 | 0.77 | 0.52 |
| 11-27 08:01 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 11-27 08:01 | +20 | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-27 08:01 | +15 | ETH | DOWN | 0.59 | yes | -6.03 |
