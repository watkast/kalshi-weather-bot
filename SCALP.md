# Range-Scalp Bot

*Updated Sat Oct 31 04:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41772 | 36446 | 5326 (54) | 0 | $-11741.32 | -4.5% |
| **+10¢** | 31136 | 24972 | 6164 (78) | 0 | $-10493.66 | -5.4% |
| **+15¢** | 26025 | 19379 | 6646 (106) | 0 | $-9590.43 | -5.9% |
| **+20¢** | 23108 | 16148 | 6960 (137) | 0 | $-8452.01 | -5.8% |
| **+10¢ (15¢ stop)** | 50918 | 50843 | 75 (41) | 0 | $-19210.80 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 04:33 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-31 04:33 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-31 04:33 | +5 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-31 04:33 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-31 04:33 | +10 stop | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:33 | +20 | SOL | DOWN | 0.64 | 0.89 | 2.26 |
| 10-31 04:33 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:33 | +10 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:33 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 10-31 04:31 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-31 04:31 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 04:31 | +20 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-31 04:31 | +15 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-31 04:31 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 04:31 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-31 04:31 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-31 04:31 | +20 | HYPE | DOWN | 0.53 | 0.80 | 2.40 |
| 10-31 04:31 | +15 | HYPE | DOWN | 0.53 | 0.80 | 2.40 |
| 10-31 04:31 | +10 | HYPE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-31 04:31 | +5 | HYPE | DOWN | 0.53 | 0.60 | 0.35 |
| 10-31 04:31 | +10 stop | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:31 | +20 | ETH | DOWN | 0.64 | 0.88 | 2.15 |
| 10-31 04:31 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:31 | +10 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 04:31 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-31 04:31 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 10-31 04:31 | +20 | BNB | DOWN | 0.70 | 0.92 | 2.00 |
| 10-31 04:31 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 10-31 04:31 | +10 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 10-31 04:31 | +5 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 10-31 04:31 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-31 04:31 | +20 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 04:31 | +15 | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-31 04:31 | +10 | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-31 04:31 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-31 04:30 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 10-31 04:30 | +20 | NEAR | DOWN | 0.70 | 0.92 | 1.99 |
| 10-31 04:30 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-31 04:30 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 10-31 04:30 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
