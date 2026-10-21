# Range-Scalp Bot

*Updated Wed Oct 21 23:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27872 | 24283 | 3589 (39) | 1 | $-8026.87 | -4.6% |
| **+10¢** | 20943 | 16800 | 4143 (55) | 3 | $-7055.19 | -5.4% |
| **+15¢** | 17539 | 13080 | 4459 (78) | 4 | $-6294.19 | -5.7% |
| **+20¢** | 15530 | 10857 | 4673 (98) | 4 | $-5623.12 | -5.8% |
| **+10¢ (15¢ stop)** | 34214 | 34155 | 59 (32) | 0 | $-12742.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 23:12 | +10 stop | NEAR | DOWN | 0.66 | 0.44 | -2.54 |
| 10-21 23:12 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-21 23:12 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-21 23:12 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-21 23:12 | +5 | NEAR | DOWN | 0.67 | open |  |
| 10-21 23:03 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 23:03 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 23:03 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 10-21 23:02 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-21 23:02 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-21 23:02 | +10 | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-21 23:02 | +5 | HYPE | DOWN | 0.65 | 0.73 | 0.46 |
| 10-21 23:02 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-21 23:02 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-21 23:02 | +15 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-21 23:02 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-21 23:02 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-21 23:02 | +10 stop | HYPE | UP | 0.44 | 0.57 | 0.94 |
| 10-21 23:02 | +10 | HYPE | UP | 0.44 | 0.57 | 0.94 |
| 10-21 23:02 | +5 | HYPE | UP | 0.44 | 0.57 | 0.94 |
| 10-21 23:02 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-21 23:02 | +20 | BTC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-21 23:02 | +15 | BTC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-21 23:02 | +10 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-21 23:02 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-21 23:02 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 23:02 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 10-21 23:02 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-21 23:02 | +10 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 23:02 | +5 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 23:01 | +5 | BNB | DOWN | 0.55 | 0.64 | 0.55 |
| 10-21 23:01 | +10 stop | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-21 23:01 | +20 | ZEC | DOWN | 0.55 | 0.78 | 1.99 |
| 10-21 23:01 | +15 | ZEC | DOWN | 0.55 | 0.70 | 1.17 |
| 10-21 23:01 | +10 | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-21 23:01 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-21 23:01 | +10 stop | HYPE | UP | 0.55 | 0.65 | 0.66 |
| 10-21 23:01 | +20 | HYPE | UP | 0.55 | open |  |
| 10-21 23:01 | +15 | HYPE | UP | 0.55 | open |  |
| 10-21 23:01 | +10 | HYPE | UP | 0.55 | 0.65 | 0.66 |
