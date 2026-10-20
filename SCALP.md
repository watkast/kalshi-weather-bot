# Range-Scalp Bot

*Updated Tue Oct 20 18:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25999 | 22642 | 3357 (32) | 0 | $-7594.33 | -4.6% |
| **+10¢** | 19570 | 15689 | 3881 (47) | 0 | $-6729.04 | -5.5% |
| **+15¢** | 16386 | 12211 | 4175 (71) | 0 | $-5995.57 | -5.8% |
| **+20¢** | 14497 | 10121 | 4376 (90) | 1 | $-5382.58 | -5.9% |
| **+10¢ (15¢ stop)** | 31890 | 31837 | 53 (30) | 0 | $-11748.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 18:02 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-20 18:02 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-20 18:02 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 18:02 | +20 | ZEC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-20 18:02 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-20 18:02 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 18:02 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 18:01 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-20 18:01 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 18:01 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-20 18:01 | +15 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 10-20 18:01 | +10 | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 18:01 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 10-20 18:01 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 18:01 | +20 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 10-20 18:01 | +15 | ETH | DOWN | 0.59 | 0.77 | 1.50 |
| 10-20 18:01 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 18:01 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-20 18:01 | +10 stop | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 18:01 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-20 18:01 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 18:01 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 18:01 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-20 18:01 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-20 18:01 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-20 18:01 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-20 18:01 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-20 18:01 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-20 18:01 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-20 18:01 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-20 18:01 | +15 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 10-20 18:01 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-20 18:01 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 10-20 18:01 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 18:01 | +20 | SOL | DOWN | 0.63 | 0.84 | 1.83 |
| 10-20 18:01 | +15 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 10-20 18:01 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 18:01 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-20 18:01 | +10 stop | HYPE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-20 18:01 | +20 | HYPE | DOWN | 0.64 | 0.87 | 2.05 |
