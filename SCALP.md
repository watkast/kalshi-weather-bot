# Range-Scalp Bot

*Updated Sat Nov 21 15:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67520 | 58929 | 8591 (134) | 0 | $-18107.50 | -4.3% |
| **+10¢** | 50427 | 40389 | 10038 (175) | 0 | $-16805.98 | -5.3% |
| **+15¢** | 42284 | 31464 | 10820 (225) | 0 | $-15046.97 | -5.7% |
| **+20¢** | 37635 | 26265 | 11370 (283) | 0 | $-13364.32 | -5.7% |
| **+10¢ (15¢ stop)** | 82188 | 82017 | 171 (105) | 0 | $-30164.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 15:22 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-21 15:22 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-21 15:21 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-21 15:21 | +10 stop | BTC | DOWN | 0.54 | 0.68 | 1.06 |
| 11-21 15:21 | +20 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-21 15:21 | +15 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-21 15:21 | +10 | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-21 15:21 | +5 | BTC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-21 15:12 | +10 stop | XRP | UP | 0.69 | 0.85 | 1.36 |
| 11-21 15:12 | +5 | XRP | UP | 0.69 | 0.78 | 0.62 |
| 11-21 15:12 | +20 | BTC | DOWN | 0.67 | 0.95 | 2.59 |
| 11-21 15:12 | +15 | BTC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-21 15:12 | +5 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 15:12 | +10 stop | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 11-21 15:12 | +5 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-21 15:11 | +10 stop | ETH | UP | 0.66 | 0.80 | 1.12 |
| 11-21 15:11 | +10 stop | HYPE | DOWN | 0.62 | 0.44 | -2.17 |
| 11-21 15:11 | +20 | HYPE | DOWN | 0.62 | yes | -6.39 |
| 11-21 15:11 | +15 | HYPE | DOWN | 0.62 | yes | -6.36 |
| 11-21 15:11 | +10 | HYPE | DOWN | 0.62 | yes | -6.36 |
| 11-21 15:11 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.39 |
| 11-21 15:10 | +10 stop | ZEC | DOWN | 0.51 | 0.33 | -2.14 |
| 11-21 15:10 | +5 | ZEC | DOWN | 0.51 | 0.57 | 0.24 |
| 11-21 15:10 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 15:10 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 15:10 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-21 15:08 | +10 stop | BTC | DOWN | 0.52 | 0.63 | 0.75 |
| 11-21 15:08 | +10 stop | XRP | UP | 0.58 | 0.38 | -2.35 |
| 11-21 15:08 | +10 stop | BNB | DOWN | 0.61 | 0.82 | 1.78 |
| 11-21 15:07 | +10 stop | ETH | UP | 0.66 | 0.47 | -2.24 |
| 11-21 15:07 | +5 | ETH | UP | 0.66 | 0.80 | 1.12 |
| 11-21 15:06 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 11-21 15:06 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-21 15:06 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-21 15:06 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-21 15:06 | +10 stop | ZEC | UP | 0.50 | 0.28 | -2.53 |
| 11-21 15:05 | +10 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-21 15:05 | +5 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-21 15:05 | +10 stop | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-21 15:05 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
