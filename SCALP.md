# Range-Scalp Bot

*Updated Sun Nov 08 07:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52158 | 45474 | 6684 (82) | 0 | $-14477.76 | -4.4% |
| **+10¢** | 38931 | 31138 | 7793 (107) | 0 | $-13486.09 | -5.5% |
| **+15¢** | 32605 | 24206 | 8399 (137) | 0 | $-12365.25 | -6.0% |
| **+20¢** | 29007 | 20203 | 8804 (181) | 0 | $-10892.44 | -6.0% |
| **+10¢ (15¢ stop)** | 63492 | 63387 | 105 (62) | 0 | $-23466.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 07:43 | +10 stop | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 11-08 07:43 | +5 | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 11-08 07:41 | +10 stop | HYPE | DOWN | 0.48 | 0.26 | -2.52 |
| 11-08 07:41 | +20 | HYPE | DOWN | 0.48 | yes | -4.98 |
| 11-08 07:41 | +15 | HYPE | DOWN | 0.46 | yes | -4.78 |
| 11-08 07:41 | +5 | HYPE | DOWN | 0.48 | 0.53 | 0.14 |
| 11-08 07:40 | +5 | BNB | DOWN | 0.65 | yes | -6.66 |
| 11-08 07:40 | +10 stop | NEAR | DOWN | 0.63 | 0.78 | 1.20 |
| 11-08 07:39 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-08 07:39 | +10 | HYPE | DOWN | 0.64 | yes | -6.57 |
| 11-08 07:38 | +10 stop | BNB | DOWN | 0.60 | 0.01 | -6.04 |
| 11-08 07:38 | +15 | BNB | DOWN | 0.61 | yes | -6.27 |
| 11-08 07:38 | +10 | BNB | DOWN | 0.61 | yes | -6.27 |
| 11-08 07:38 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 11-08 07:38 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-08 07:38 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.69 |
| 11-08 07:38 | +10 stop | NEAR | UP | 0.53 | 0.37 | -1.95 |
| 11-08 07:37 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.97 |
| 11-08 07:35 | +10 stop | XRP | UP | 0.68 | 0.84 | 1.35 |
| 11-08 07:35 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.84 |
| 11-08 07:34 | +10 stop | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 11-08 07:34 | +5 | DOGE | UP | 0.64 | 0.73 | 0.59 |
| 11-08 07:34 | +10 stop | ETH | UP | 0.67 | 0.77 | 0.71 |
| 11-08 07:33 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-08 07:33 | +10 stop | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-08 07:33 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-08 07:32 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-08 07:32 | +10 stop | BTC | UP | 0.56 | 0.74 | 1.48 |
| 11-08 07:32 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 11-08 07:32 | +20 | XRP | DOWN | 0.64 | yes | -6.57 |
| 11-08 07:32 | +15 | XRP | DOWN | 0.64 | yes | -6.57 |
| 11-08 07:32 | +10 | XRP | DOWN | 0.64 | yes | -6.57 |
| 11-08 07:32 | +5 | XRP | DOWN | 0.64 | yes | -6.57 |
| 11-08 07:32 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 11-08 07:32 | +20 | NEAR | DOWN | 0.65 | 0.95 | 2.77 |
| 11-08 07:32 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 07:32 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-08 07:32 | +5 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-08 07:31 | +10 stop | HYPE | DOWN | 0.49 | 0.31 | -2.13 |
| 11-08 07:31 | +20 | HYPE | DOWN | 0.49 | 0.71 | 1.87 |
