# Range-Scalp Bot

*Updated Sun Oct 25 15:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33333 | 29077 | 4256 (42) | 0 | $-9405.81 | -4.5% |
| **+10¢** | 24954 | 20030 | 4924 (60) | 0 | $-8359.73 | -5.3% |
| **+15¢** | 20879 | 15577 | 5302 (83) | 0 | $-7547.25 | -5.8% |
| **+20¢** | 18501 | 12950 | 5551 (105) | 0 | $-6655.51 | -5.7% |
| **+10¢ (15¢ stop)** | 40875 | 40815 | 60 (32) | 0 | $-15606.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 15:22 | +5 | ZEC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-25 15:20 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-25 15:20 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 15:20 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-25 15:20 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-25 15:20 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 15:20 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-25 15:19 | +5 | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-25 15:18 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-25 15:18 | +10 stop | BNB | DOWN | 0.51 | 0.72 | 1.77 |
| 10-25 15:18 | +20 | BNB | DOWN | 0.51 | 0.72 | 1.77 |
| 10-25 15:18 | +15 | BNB | DOWN | 0.51 | 0.72 | 1.77 |
| 10-25 15:18 | +10 | BNB | DOWN | 0.52 | 0.72 | 1.67 |
| 10-25 15:18 | +5 | BNB | DOWN | 0.52 | 0.59 | 0.35 |
| 10-25 15:17 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-25 15:17 | +20 | BTC | DOWN | 0.67 | 0.90 | 2.11 |
| 10-25 15:17 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-25 15:17 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-25 15:17 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-25 15:16 | +10 stop | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 15:16 | +20 | ZEC | DOWN | 0.58 | 0.84 | 2.32 |
| 10-25 15:16 | +15 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 15:16 | +10 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 15:16 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.46 |
| 10-25 15:16 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-25 15:16 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 10-25 15:16 | +15 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 10-25 15:16 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-25 15:16 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 10-25 15:16 | +10 stop | ETH | DOWN | 0.64 | 0.80 | 1.32 |
| 10-25 15:16 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.74 |
| 10-25 15:16 | +15 | ETH | DOWN | 0.64 | 0.80 | 1.32 |
| 10-25 15:16 | +10 | ETH | DOWN | 0.64 | 0.80 | 1.32 |
| 10-25 15:16 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.19 |
| 10-25 15:16 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-25 15:16 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-25 15:16 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-25 15:16 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-25 15:16 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-25 15:16 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
