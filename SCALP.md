# Range-Scalp Bot

*Updated Sun Nov 01 16:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43673 | 38057 | 5616 (64) | 0 | $-12447.95 | -4.5% |
| **+10¢** | 32589 | 26103 | 6486 (85) | 0 | $-11159.99 | -5.4% |
| **+15¢** | 27276 | 20289 | 6987 (112) | 0 | $-10206.18 | -6.0% |
| **+20¢** | 24220 | 16900 | 7320 (146) | 0 | $-9015.52 | -5.9% |
| **+10¢ (15¢ stop)** | 53276 | 53190 | 86 (51) | 0 | $-20103.11 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 16:34 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 16:34 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.80 |
| 11-01 16:34 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-01 16:34 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 16:34 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-01 16:33 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-01 16:33 | +10 | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 11-01 16:33 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 11-01 16:33 | +10 stop | BNB | DOWN | 0.69 | 0.90 | 1.89 |
| 11-01 16:33 | +10 | BNB | DOWN | 0.69 | 0.90 | 1.89 |
| 11-01 16:33 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 11-01 16:32 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-01 16:32 | +20 | BTC | DOWN | 0.69 | 0.92 | 2.05 |
| 11-01 16:32 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 16:32 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-01 16:32 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-01 16:31 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 16:31 | +20 | BNB | DOWN | 0.61 | 0.90 | 2.67 |
| 11-01 16:31 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 16:31 | +10 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 16:31 | +5 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 16:30 | +10 stop | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-01 16:30 | +20 | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 11-01 16:30 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 16:30 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 11-01 16:30 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 11-01 16:30 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 16:30 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-01 16:30 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-01 16:30 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 16:30 | +5 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 16:22 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 11-01 16:21 | +10 stop | ETH | UP | 0.66 | 0.80 | 1.12 |
| 11-01 16:21 | +20 | ETH | UP | 0.66 | 0.93 | 2.53 |
| 11-01 16:21 | +15 | ETH | UP | 0.66 | 0.82 | 1.33 |
| 11-01 16:21 | +10 | ETH | UP | 0.66 | 0.80 | 1.12 |
| 11-01 16:21 | +5 | ETH | UP | 0.66 | 0.80 | 1.12 |
| 11-01 16:19 | +10 stop | XRP | DOWN | 0.62 | 0.39 | -2.64 |
| 11-01 16:19 | +5 | HYPE | UP | 0.69 | 0.77 | 0.52 |
| 11-01 16:19 | +10 stop | ZEC | UP | 0.65 | 0.84 | 1.64 |
