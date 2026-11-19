# Range-Scalp Bot

*Updated Thu Nov 19 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64623 | 56380 | 8243 (124) | 0 | $-17527.28 | -4.3% |
| **+10¢** | 48275 | 38632 | 9643 (165) | 1 | $-16342.26 | -5.4% |
| **+15¢** | 40481 | 30084 | 10397 (210) | 1 | $-14768.65 | -5.8% |
| **+20¢** | 36050 | 25133 | 10917 (265) | 3 | $-13074.48 | -5.8% |
| **+10¢ (15¢ stop)** | 78622 | 78458 | 164 (98) | 0 | $-28876.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 02:35 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 02:35 | +10 stop | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-19 02:35 | +10 | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-19 02:35 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 11-19 02:34 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 11-19 02:34 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.95 |
| 11-19 02:34 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-19 02:34 | +5 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-19 02:34 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.23 |
| 11-19 02:34 | +10 stop | NEAR | DOWN | 0.60 | 0.79 | 1.64 |
| 11-19 02:33 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 11-19 02:33 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-19 02:32 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-19 02:32 | +20 | HYPE | DOWN | 0.57 | 0.81 | 2.11 |
| 11-19 02:32 | +15 | HYPE | DOWN | 0.57 | 0.81 | 2.11 |
| 11-19 02:32 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-19 02:32 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-19 02:32 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 02:32 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 02:32 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 11-19 02:32 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-19 02:32 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 02:32 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-19 02:32 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-19 02:32 | +20 | SOL | DOWN | 0.61 | 0.85 | 2.14 |
| 11-19 02:32 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 11-19 02:32 | +10 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-19 02:32 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 11-19 02:32 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-19 02:32 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-19 02:32 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-19 02:32 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-19 02:32 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-19 02:32 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-19 02:32 | +20 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-19 02:32 | +15 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-19 02:32 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-19 02:32 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-19 02:32 | +10 stop | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 11-19 02:32 | +20 | BNB | DOWN | 0.67 | open |  |
