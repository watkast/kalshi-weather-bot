# Range-Scalp Bot

*Updated Sat Nov 21 08:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67309 | 58752 | 8557 (129) | 0 | $-18032.32 | -4.3% |
| **+10¢** | 50266 | 40267 | 9999 (171) | 0 | $-16728.34 | -5.3% |
| **+15¢** | 42160 | 31379 | 10781 (219) | 0 | $-14997.80 | -5.7% |
| **+20¢** | 37525 | 26196 | 11329 (276) | 0 | $-13320.54 | -5.7% |
| **+10¢ (15¢ stop)** | 81945 | 81779 | 166 (100) | 0 | $-30120.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 08:32 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-21 08:32 | +10 stop | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-21 08:32 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 11-21 08:32 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-21 08:32 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-21 08:32 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-21 08:32 | +5 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-21 08:32 | +10 stop | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-21 08:32 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-21 08:32 | +15 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-21 08:32 | +10 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-21 08:32 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-21 08:32 | +10 stop | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-21 08:32 | +20 | XRP | DOWN | 0.57 | 0.79 | 1.90 |
| 11-21 08:32 | +15 | XRP | DOWN | 0.57 | 0.79 | 1.90 |
| 11-21 08:32 | +10 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-21 08:32 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 11-21 08:32 | +10 stop | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 11-21 08:32 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.81 |
| 11-21 08:32 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.39 |
| 11-21 08:32 | +10 | BNB | DOWN | 0.61 | 0.78 | 1.39 |
| 11-21 08:32 | +5 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 11-21 08:31 | +10 stop | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-21 08:31 | +20 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 11-21 08:31 | +15 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 11-21 08:31 | +10 | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-21 08:31 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-21 08:31 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 08:31 | +20 | ZEC | DOWN | 0.59 | 0.80 | 1.81 |
| 11-21 08:31 | +15 | ZEC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-21 08:31 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 08:31 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-21 08:31 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-21 08:31 | +20 | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 11-21 08:31 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-21 08:31 | +10 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-21 08:31 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 11-21 08:31 | +10 stop | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-21 08:31 | +20 | HYPE | DOWN | 0.56 | 0.80 | 2.10 |
| 11-21 08:31 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
