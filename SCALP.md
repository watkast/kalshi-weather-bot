# Range-Scalp Bot

*Updated Tue Nov 24 01:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70423 | 61468 | 8955 (147) | 1 | $-18833.86 | -4.2% |
| **+10¢** | 52540 | 42083 | 10457 (190) | 1 | $-17457.28 | -5.3% |
| **+15¢** | 44014 | 32751 | 11263 (246) | 1 | $-15541.55 | -5.6% |
| **+20¢** | 39191 | 27335 | 11856 (311) | 2 | $-13911.74 | -5.7% |
| **+10¢ (15¢ stop)** | 85756 | 85560 | 196 (118) | 0 | $-31534.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 01:46 | +10 stop | BNB | UP | 0.36 | 0.57 | 1.75 |
| 11-24 01:46 | +20 | BNB | UP | 0.37 | 0.57 | 1.65 |
| 11-24 01:46 | +15 | BNB | UP | 0.37 | 0.57 | 1.65 |
| 11-24 01:46 | +10 | BNB | UP | 0.38 | 0.57 | 1.55 |
| 11-24 01:46 | +5 | BNB | UP | 0.38 | 0.57 | 1.55 |
| 11-24 01:46 | +10 stop | ETH | UP | 0.36 | 0.54 | 1.45 |
| 11-24 01:46 | +20 | ETH | UP | 0.36 | open |  |
| 11-24 01:46 | +15 | ETH | UP | 0.37 | 0.54 | 1.35 |
| 11-24 01:46 | +10 | ETH | UP | 0.37 | 0.54 | 1.35 |
| 11-24 01:46 | +5 | ETH | UP | 0.37 | 0.54 | 1.35 |
| 11-24 01:46 | +10 stop | NEAR | UP | 0.34 | 0.57 | 1.96 |
| 11-24 01:46 | +20 | NEAR | UP | 0.34 | 0.57 | 1.96 |
| 11-24 01:46 | +15 | NEAR | UP | 0.34 | 0.57 | 1.96 |
| 11-24 01:46 | +10 | NEAR | UP | 0.34 | 0.57 | 1.96 |
| 11-24 01:46 | +5 | NEAR | UP | 0.34 | 0.57 | 1.96 |
| 11-24 01:45 | +10 stop | HYPE | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 01:45 | +20 | HYPE | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 01:45 | +15 | HYPE | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 01:45 | +10 | HYPE | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 01:45 | +5 | HYPE | DOWN | 0.51 | 0.77 | 2.29 |
| 11-24 01:45 | +10 stop | BTC | UP | 0.64 | 0.33 | -3.43 |
| 11-24 01:45 | +20 | BTC | UP | 0.63 | open |  |
| 11-24 01:45 | +15 | BTC | UP | 0.63 | open |  |
| 11-24 01:45 | +10 | BTC | UP | 0.62 | open |  |
| 11-24 01:45 | +5 | BTC | UP | 0.62 | open |  |
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
