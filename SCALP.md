# Range-Scalp Bot

*Updated Mon Oct 26 08:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34514 | 30127 | 4387 (43) | 0 | $-9596.18 | -4.4% |
| **+10¢** | 25837 | 20763 | 5074 (65) | 0 | $-8423.98 | -5.2% |
| **+15¢** | 21611 | 16149 | 5462 (89) | 0 | $-7544.38 | -5.6% |
| **+20¢** | 19153 | 13426 | 5727 (112) | 1 | $-6673.35 | -5.5% |
| **+10¢ (15¢ stop)** | 42283 | 42221 | 62 (33) | 0 | $-16098.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 08:02 | +10 stop | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-26 08:02 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-26 08:02 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-26 08:02 | +10 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-26 08:02 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-26 08:01 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 08:01 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-26 08:01 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 10-26 08:01 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 08:01 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-26 08:01 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 08:01 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.13 |
| 10-26 08:01 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-26 08:01 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 08:01 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 08:01 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 08:01 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-26 08:01 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-26 08:01 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-26 08:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-26 08:01 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 08:01 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 10-26 08:01 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 08:01 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 08:01 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.74 |
| 10-26 08:01 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 08:01 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-26 08:01 | +15 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-26 08:01 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 08:01 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-26 08:01 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 08:01 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 10-26 08:01 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 08:01 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 08:01 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 10-26 08:00 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.74 |
| 10-26 08:00 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.90 |
| 10-26 08:00 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 10-26 08:00 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.74 |
| 10-26 08:00 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
