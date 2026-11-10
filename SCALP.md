# Range-Scalp Bot

*Updated Tue Nov 10 08:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54430 | 47474 | 6956 (89) | 0 | $-14870.22 | -4.3% |
| **+10¢** | 40673 | 32559 | 8114 (117) | 1 | $-13808.96 | -5.4% |
| **+15¢** | 34091 | 25342 | 8749 (150) | 1 | $-12589.12 | -5.9% |
| **+20¢** | 30357 | 21181 | 9176 (198) | 1 | $-10985.78 | -5.8% |
| **+10¢ (15¢ stop)** | 66324 | 66214 | 110 (66) | 0 | $-24527.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 08:25 | +5 | BNB | DOWN | 0.56 | 0.64 | 0.45 |
| 11-10 08:24 | +10 stop | BNB | DOWN | 0.64 | 0.48 | -1.95 |
| 11-10 08:24 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-10 08:24 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-10 08:24 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 11-10 08:22 | +10 stop | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 11-10 08:22 | +15 | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 11-10 08:22 | +10 | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 11-10 08:22 | +5 | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 11-10 08:21 | +5 | XRP | DOWN | 0.67 | 0.93 | 2.42 |
| 11-10 08:20 | +10 stop | XRP | DOWN | 0.65 | 0.93 | 2.62 |
| 11-10 08:20 | +10 | XRP | DOWN | 0.65 | 0.93 | 2.62 |
| 11-10 08:20 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 11-10 08:20 | +10 stop | BNB | DOWN | 0.57 | 0.40 | -2.05 |
| 11-10 08:20 | +5 | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 11-10 08:20 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-10 08:20 | +5 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-10 08:19 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-10 08:18 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 08:17 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-10 08:17 | +20 | XRP | DOWN | 0.62 | 0.93 | 2.91 |
| 11-10 08:17 | +15 | XRP | DOWN | 0.62 | 0.93 | 2.91 |
| 11-10 08:17 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-10 08:17 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-10 08:16 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 11-10 08:16 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-10 08:16 | +15 | BNB | DOWN | 0.59 | 0.77 | 1.50 |
| 11-10 08:16 | +10 | BNB | DOWN | 0.59 | 0.77 | 1.50 |
| 11-10 08:16 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-10 08:16 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 08:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-10 08:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-10 08:16 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-10 08:16 | +5 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-10 08:16 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 08:16 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.83 |
| 11-10 08:16 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-10 08:16 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 11-10 08:16 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 11-10 08:16 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
