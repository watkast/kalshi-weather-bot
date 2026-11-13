# Range-Scalp Bot

*Updated Fri Nov 13 01:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57563 | 50197 | 7366 (101) | 1 | $-15728.21 | -4.3% |
| **+10¢** | 43027 | 34422 | 8605 (133) | 1 | $-14693.83 | -5.4% |
| **+15¢** | 36071 | 26810 | 9261 (167) | 1 | $-13258.18 | -5.9% |
| **+20¢** | 32138 | 22421 | 9717 (217) | 1 | $-11617.60 | -5.8% |
| **+10¢ (15¢ stop)** | 70189 | 70061 | 128 (78) | 0 | $-25847.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 01:11 | +10 stop | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 11-13 01:11 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.15 |
| 11-13 01:11 | +15 | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 11-13 01:11 | +10 | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 11-13 01:11 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 11-13 01:04 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.75 |
| 11-13 01:02 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-13 01:02 | +20 | DOGE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-13 01:02 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-13 01:02 | +10 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-13 01:02 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-13 01:02 | +10 stop | ZEC | UP | 0.60 | 0.37 | -2.64 |
| 11-13 01:01 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-13 01:01 | +20 | BTC | DOWN | 0.70 | 0.93 | 2.09 |
| 11-13 01:01 | +15 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-13 01:01 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-13 01:01 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-13 01:01 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-13 01:01 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-13 01:01 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 11-13 01:01 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-13 01:01 | +5 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-13 01:01 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 01:01 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-13 01:01 | +15 | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-13 01:01 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-13 01:01 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-13 01:01 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-13 01:01 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.80 |
| 11-13 01:01 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-13 01:01 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-13 01:01 | +5 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-13 01:01 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-13 01:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-13 01:01 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-13 01:01 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-13 01:01 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-13 01:01 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 01:01 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-13 01:01 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
