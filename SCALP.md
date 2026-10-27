# Range-Scalp Bot

*Updated Tue Oct 27 03:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35908 | 31341 | 4567 (43) | 0 | $-10027.18 | -4.4% |
| **+10¢** | 26846 | 21565 | 5281 (65) | 2 | $-8856.45 | -5.2% |
| **+15¢** | 22460 | 16787 | 5673 (89) | 4 | $-7867.90 | -5.6% |
| **+20¢** | 19906 | 13963 | 5943 (112) | 5 | $-6911.37 | -5.5% |
| **+10¢ (15¢ stop)** | 44019 | 43956 | 63 (33) | 0 | $-16735.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 03:05 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 03:05 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 03:05 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-27 03:05 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 03:05 | +5 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 03:04 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.90 |
| 10-27 03:04 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 03:04 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 10-27 03:04 | +10 stop | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-27 03:04 | +10 | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-27 03:04 | +5 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-27 03:03 | +5 | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-27 03:02 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-27 03:02 | +10 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-27 03:02 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 10-27 03:02 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 03:02 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-27 03:02 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 10-27 03:02 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 03:02 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 03:02 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 03:02 | +20 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 10-27 03:02 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 03:02 | +10 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 03:02 | +5 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-27 03:02 | +10 stop | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-27 03:02 | +20 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-27 03:02 | +15 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-27 03:02 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 03:02 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-27 03:02 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-27 03:01 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-27 03:01 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 03:01 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-27 03:01 | +5 | HYPE | DOWN | 0.62 | 0.74 | 0.85 |
| 10-27 03:01 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 10-27 03:01 | +10 | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 10-27 03:01 | +5 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 03:01 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
| 10-27 03:01 | +10 stop | ZEC | UP | 0.60 | 0.30 | -3.32 |
