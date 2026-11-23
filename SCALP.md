# Range-Scalp Bot

*Updated Mon Nov 23 20:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70081 | 61156 | 8925 (147) | 9 | $-18846.39 | -4.3% |
| **+10¢** | 52288 | 41864 | 10424 (190) | 8 | $-17498.17 | -5.3% |
| **+15¢** | 43813 | 32586 | 11227 (246) | 9 | $-15595.84 | -5.7% |
| **+20¢** | 39007 | 27192 | 11815 (311) | 9 | $-13967.04 | -5.7% |
| **+10¢ (15¢ stop)** | 85356 | 85160 | 196 (118) | 7 | $-31385.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 20:47 | +10 stop | BTC | UP | 0.50 | open |  |
| 11-23 20:47 | +10 stop | ZEC | UP | 0.67 | open |  |
| 11-23 20:47 | +20 | ZEC | UP | 0.67 | open |  |
| 11-23 20:47 | +15 | ZEC | UP | 0.67 | open |  |
| 11-23 20:47 | +10 | ZEC | UP | 0.67 | open |  |
| 11-23 20:47 | +5 | ZEC | UP | 0.67 | open |  |
| 11-23 20:47 | +10 stop | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 11-23 20:47 | +10 | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 11-23 20:47 | +15 | BNB | DOWN | 0.53 | open |  |
| 11-23 20:47 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-23 20:47 | +10 stop | SOL | DOWN | 0.51 | open |  |
| 11-23 20:47 | +10 | SOL | DOWN | 0.50 | open |  |
| 11-23 20:47 | +10 stop | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 11-23 20:47 | +10 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-23 20:47 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-23 20:47 | +10 stop | HYPE | DOWN | 0.64 | open |  |
| 11-23 20:47 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-23 20:47 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 11-23 20:47 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-23 20:47 | +5 | HYPE | DOWN | 0.68 | open |  |
| 11-23 20:46 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-23 20:46 | +10 stop | BTC | DOWN | 0.61 | 0.44 | -2.05 |
| 11-23 20:46 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-23 20:46 | +15 | BTC | DOWN | 0.61 | open |  |
| 11-23 20:46 | +10 | BTC | DOWN | 0.61 | open |  |
| 11-23 20:46 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-23 20:46 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-23 20:46 | +10 stop | DOGE | DOWN | 0.68 | 0.47 | -2.44 |
| 11-23 20:46 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-23 20:46 | +15 | DOGE | DOWN | 0.71 | open |  |
| 11-23 20:46 | +10 | DOGE | DOWN | 0.71 | open |  |
| 11-23 20:46 | +5 | DOGE | DOWN | 0.71 | open |  |
| 11-23 20:46 | +10 stop | XRP | DOWN | 0.63 | open |  |
| 11-23 20:46 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-23 20:46 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-23 20:46 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-23 20:46 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-23 20:46 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-23 20:46 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 11-23 20:46 | +20 | NEAR | DOWN | 0.65 | open |  |
