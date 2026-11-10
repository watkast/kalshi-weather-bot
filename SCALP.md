# Range-Scalp Bot

*Updated Tue Nov 10 02:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54183 | 47270 | 6913 (89) | 0 | $-14723.96 | -4.3% |
| **+10¢** | 40478 | 32410 | 8068 (117) | 0 | $-13677.89 | -5.4% |
| **+15¢** | 33926 | 25231 | 8695 (149) | 0 | $-12430.13 | -5.8% |
| **+20¢** | 30208 | 21089 | 9119 (195) | 0 | $-10836.58 | -5.7% |
| **+10¢ (15¢ stop)** | 66009 | 65899 | 110 (66) | 0 | $-24415.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 02:21 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 11-10 02:20 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-10 02:17 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-10 02:17 | +20 | BTC | DOWN | 0.66 | 0.91 | 2.22 |
| 11-10 02:17 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-10 02:17 | +10 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-10 02:17 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 02:17 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.75 |
| 11-10 02:17 | +20 | BNB | DOWN | 0.67 | 0.90 | 2.11 |
| 11-10 02:17 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.68 |
| 11-10 02:17 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.75 |
| 11-10 02:17 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.22 |
| 11-10 02:17 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 02:17 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-10 02:17 | +15 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 02:17 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 02:17 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-10 02:16 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:16 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.85 |
| 11-10 02:16 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-10 02:16 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:16 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-10 02:16 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:16 | +20 | XRP | DOWN | 0.70 | 0.92 | 1.98 |
| 11-10 02:16 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 02:16 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:16 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 11-10 02:16 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 02:16 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 11-10 02:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 02:16 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 02:16 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 02:16 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-10 02:16 | +20 | HYPE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-10 02:16 | +15 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-10 02:16 | +10 | HYPE | DOWN | 0.61 | 0.73 | 0.93 |
| 11-10 02:16 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.21 |
| 11-10 02:16 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-10 02:16 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 11-10 02:16 | +15 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
