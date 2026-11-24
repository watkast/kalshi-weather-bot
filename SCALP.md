# Range-Scalp Bot

*Updated Tue Nov 24 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70419 | 61464 | 8955 (147) | 0 | $-18841.01 | -4.3% |
| **+10¢** | 52536 | 42079 | 10457 (190) | 0 | $-17464.43 | -5.3% |
| **+15¢** | 44010 | 32747 | 11263 (246) | 0 | $-15548.80 | -5.6% |
| **+20¢** | 39187 | 27331 | 11856 (311) | 1 | $-13920.88 | -5.7% |
| **+10¢ (15¢ stop)** | 85751 | 85555 | 196 (118) | 0 | $-31538.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 01:43 | +10 stop | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 11-24 01:39 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 01:39 | +10 stop | XRP | UP | 0.64 | 0.44 | -2.35 |
| 11-24 01:38 | +10 stop | BNB | DOWN | 0.58 | 0.82 | 2.11 |
| 11-24 01:38 | +15 | BNB | DOWN | 0.58 | 0.82 | 2.11 |
| 11-24 01:38 | +10 | BNB | DOWN | 0.58 | 0.82 | 2.11 |
| 11-24 01:38 | +5 | BNB | DOWN | 0.58 | 0.82 | 2.11 |
| 11-24 01:38 | +10 stop | DOGE | DOWN | 0.61 | 0.41 | -2.34 |
| 11-24 01:37 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-24 01:37 | +10 stop | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-24 01:37 | +10 | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-24 01:37 | +5 | ZEC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-24 01:36 | +10 stop | DOGE | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 01:36 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-24 01:36 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 11-24 01:36 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 11-24 01:35 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-24 01:35 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-24 01:35 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 11-24 01:35 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-24 01:35 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-24 01:35 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 01:35 | +10 stop | SOL | DOWN | 0.71 | 0.54 | -2.03 |
| 11-24 01:34 | +10 stop | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 11-24 01:34 | +10 | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 11-24 01:34 | +5 | BNB | DOWN | 0.59 | 0.66 | 0.37 |
| 11-24 01:34 | +10 stop | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 11-24 01:34 | +10 | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 11-24 01:34 | +5 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-24 01:34 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +10 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +5 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +10 stop | ETH | DOWN | 0.55 | 0.66 | 0.76 |
| 11-24 01:34 | +10 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 01:34 | +5 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 01:33 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-24 01:33 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-24 01:33 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.25 |
| 11-24 01:32 | +10 stop | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 11-24 01:32 | +20 | BNB | DOWN | 0.60 | 0.82 | 1.92 |
